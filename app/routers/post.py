from typing import List,Optional
from fastapi import FastAPI, Response, status, HTTPException,Depends,APIRouter
from ..import models,schema,utils
from sqlalchemy import func
from ..database import get_db
from sqlalchemy.orm import session

from .. import database,schema,models,utils,oath2

router = APIRouter(
    prefix = "/posts",
    tags= ['Posts']

)
    
@router.get("/",response_model=List[schema.PostOut])
def test_posts(db:session =Depends(get_db),current_user:int = Depends(oath2.get_current_user),
               limit:int = 10,skip:int=0,search:Optional[str] = ""):
    
    print(limit)
    posts =db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    #cursor.execute("SELECT * FROM posts")
   #posts = cursor.fetchall()

    results = db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(models.Vote,models.Vote.post_id==models.Post.id,
                                         isouter=True).group_by(models.Post.id).all()
    formatted_results = [{"Post": post, "votes": votes} for post, votes in results]

    return formatted_results
    


@router.post("/", status_code=status.HTTP_201_CREATED,response_model=schema.Post)
def create_posts(post:schema.Postcreate,
                 db:session =Depends(get_db),current_user:int =Depends(oath2.get_current_user)):
    
    #cursor.execute(
        #"INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *",
      #  (post.title, post.content, post.published)
   # )
   # new_post = cursor.fetchone()
   # conn.commit()
   
   new_post = models.Post(owner_id = current_user.id, **post.dict())
   db.add(new_post)
   db.commit()
   db.refresh(new_post)
   return new_post

@router.get("/{id}",response_model=schema.PostOut)
def get_post(id: int,db:session =Depends(get_db),current_user:int = Depends(oath2.get_current_user)):
   # cursor.execute("SELECT * FROM posts WHERE id = %s", (id,))
    #post = cursor.fetchone()

   # post = db.query(models.Post).filter(models.Post.id==id).first()

    result = db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(models.Vote,models.Vote.post_id==models.Post.id,
                                         isouter=True).group_by(models.Post.id).filter(models.Post.id==id).first()
    post, votes = result

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} was not found"
        )

    if post.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action"
        )
    return {"Post": post, "votes": votes} 

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db:session =Depends(get_db),current_user:int = Depends(oath2.get_current_user)):
    #cursor.execute("DELETE FROM posts WHERE id = %s RETURNING *", (id,))
    #deleted_post = cursor.fetchone()
    #conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id==id)
    post = post_query.first()

    if post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} does not exist")
    
    if post.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action"
        )
    
    post_query.delete(synchronize_session =False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}",response_model=schema.Post)
def update_post(id: int, updated_post: schema.Postcreate,db:session =Depends(get_db),
                curren_user:int = Depends(oath2.get_current_user)):
        
    #cursor.execute("UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *",
       # (post.title, post.content, post.published, id))
    #updated_post = cursor.fetchone()
    #conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id==id)
    post = post_query.first()
    if post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} does not exist")
    
    if post.owner_id != curren_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform action"
        )
    
    
    post_query.update(updated_post.dict(),synchronize_session =False)
    db.commit()
    return post_query.first()
