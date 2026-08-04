from fastapi import APIRouter, Depends, HTTPException, status

from app.core.dependencies import require_role
from app.core.roles import RoleLevel
from app.repositories.user_repository import UserRepository
from app.schemas.user import (
    UserCreate,
    UserResponse,
    UserUpdate,
)
from app.services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

service = UserService()
_repo = UserRepository()

_admin_only = Depends(require_role(RoleLevel.SUPER_USER))


# ---------------- CREATE ---------------- #

@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[_admin_only],
)
async def register_user(payload: UserCreate):
    return await service.register(payload)


# ---------------- GET ALL ---------------- #

@router.get(
    "/",
    response_model=list[UserResponse],
    dependencies=[_admin_only],
)
async def list_users():
    return await _repo.get_all()


# ---------------- GET ONE ---------------- #

@router.get(
    "/{user_id}",
    response_model=UserResponse,
    dependencies=[_admin_only],
)
async def get_user(user_id: str):

    user = await _repo.get_by_id(user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user


# ---------------- UPDATE ---------------- #

@router.put(
    "/{user_id}",
    response_model=UserResponse,
    dependencies=[_admin_only],
)
async def update_user(
    user_id: str,
    payload: UserUpdate,
):
    return await service.update(
        user_id,
        payload,
    )


# ---------------- DELETE ---------------- #

@router.delete(
    "/{user_id}",
    dependencies=[_admin_only],
)
async def delete_user(user_id: str):
    return await service.delete(user_id)