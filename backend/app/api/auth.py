from fastapi import APIRouter, Depends, Request, status

from app.core.dependencies import _client_ip, login_decorator
from app.schemas.auth import CurrentUser, LoginRequest, TokenResponse
from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

service = AuthService()


@router.post(
    "/login",
    response_model=TokenResponse,
    status_code=status.HTTP_200_OK,
)
async def login(
    credentials: LoginRequest,
    request: Request,
):
    return await service.login(credentials)


@router.post("/logout")
async def logout(
    current_user: CurrentUser = Depends(login_decorator),
):
    return await service.logout(current_user)


@router.get(
    "/me",
    response_model=CurrentUser,
)
async def get_me(
    current_user: CurrentUser = Depends(login_decorator),
):
    return current_user