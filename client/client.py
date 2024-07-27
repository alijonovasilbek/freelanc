from fastapi import FastAPI, Depends, HTTPException, APIRouter
from auth.utils import verify_token
from typing import List
from database import get_async_session
from sqlalchemy import insert, update, delete
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from .schemes import Gig,GigPost
from models.models import user,gigs
from datetime import datetime
from .schemes import GigCategoryPost, GigSkillPost, GigFilePost

from .schemes import GigCategoryPost, GigCategory

from models.models import gigs_category, gigs_skill, gigs_file, user

router_client = APIRouter(tags=["Client API"])



@router_client.post('/gigs', response_model=Gig, summary="Create a Gig")
async def create_gig(new_gig: GigPost, token: dict = Depends(verify_token), session: AsyncSession = Depends(get_async_session)):
    if token is None:
        raise HTTPException(status_code=401, detail="Not registered")
    user_id = token.get('user_id')


    result = await session.execute(select(user).where(user.c.id == user_id))
    user_data = result.fetchone()
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")
    

    if not user_data.is_client:
        raise HTTPException(status_code=403, detail="Only clients can post gigs")


    new_gig_data = new_gig.dict()
    new_gig_data['user_id'] = user_id
   

    query = insert(gigs).values(**new_gig_data).returning(gigs)
    result = await session.execute(query)
    created_gig = result.fetchone()
    await session.commit()
    
    return created_gig


@router_client.get('/gigs', response_model=List[Gig], summary="Get all Gigs by User")
async def get_user_gigs(token: dict = Depends(verify_token), session: AsyncSession = Depends(get_async_session)):
    if token is None:
        raise HTTPException(status_code=401, detail="Not registered")
    user_id = token.get('user_id')

    result = await session.execute(select(gigs).where(gigs.c.user_id == user_id))
    user_gigs = result.fetchall()

    if not user_gigs:
        raise HTTPException(status_code=404, detail="No gigs found for this user")

    return user_gigs


@router_client.post('/gigs_category', summary="Create a Gig Category")
async def create_gig_category(
    new_category: GigCategoryPost,
    token: dict = Depends(verify_token),
    session: AsyncSession = Depends(get_async_session)
):
    if token is None:
        raise HTTPException(status_code=401, detail="Not registered")
    user_id = token.get('user_id')

    result = await session.execute(select(user).where(user.c.id == user_id))
    user_data = result.fetchone()
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")

    if not user_data.is_client:
        raise HTTPException(status_code=403, detail="Only clients can post categories")

    result = await session.execute(select(gigs).where(gigs.c.id == new_category.gigs_id))
    gig_data = result.fetchone()
    if not gig_data:
        raise HTTPException(status_code=404, detail="Gig not found")

    if gig_data.user_id != user_id:
        raise HTTPException(status_code=403, detail="You can only add categories to your own gigs")

    new_category_data = new_category.dict()
    query = insert(gigs_category).values(**new_category_data).returning(gigs_category)
    result = await session.execute(query)
    created_category = result.fetchone()
    await session.commit()

    if created_category:
     
        created_category_dict = {
            'id': created_category[0],
            'name': created_category[1],
            'description': created_category[2]
           
        }
  
        created_category_model = GigCategory(**created_category_dict)
        return created_category_model.dict()
    else:
        raise HTTPException(status_code=500, detail="Failed to create category")





@router_client.post('/gigs_skill', summary="Create a Gig Skill")
async def create_gig_skill(new_skill: GigSkillPost, token: dict = Depends(verify_token), session: AsyncSession = Depends(get_async_session)):
    if token is None:
        raise HTTPException(status_code=401, detail="Not registered")
    user_id = token.get('user_id')

    # Foydalanuvchini topish
    result = await session.execute(select(user).where(user.c.id == user_id))
    user_data = result.fetchone()
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Faqat mijozlar bu ma'lumotlarni qo'shishi mumkin
    if not user_data.is_client:
        raise HTTPException(status_code=403, detail="Only clients can post skills")

    new_skill_data = new_skill.dict()
    query = insert(gigs_skill).values(**new_skill_data).returning(gigs_skill)
    result = await session.execute(query)
    created_skill = result.fetchone()
    await session.commit()
    
    return created_skill

# Gig File qo'shish uchun endpoint
@router_client.post('/gigs_file', summary="Create a Gig File")
async def create_gig_file(new_file: GigFilePost, token: dict = Depends(verify_token), session: AsyncSession = Depends(get_async_session)):
    if token is None:
        raise HTTPException(status_code=401, detail="Not registered")
    user_id = token.get('user_id')

    # Foydalanuvchini topish
    result = await session.execute(select(user).where(user.c.id == user_id))
    user_data = result.fetchone()
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Faqat mijozlar bu ma'lumotlarni qo'shishi mumkin
    if not user_data.is_client:
        raise HTTPException(status_code=403, detail="Only clients can post files")

    new_file_data = new_file.dict()
    query = insert(gigs_file).values(**new_file_data).returning(gigs_file)
    result = await session.execute(query)
    created_file = result.fetchone()
    await session.commit()
    
    return created_file






