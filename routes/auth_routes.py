from fastapi import APIRouter, HTTPException

from models.auth_models import LoginForm, RegisterForm, AuthResponse

auth_router = APIRouter()

FAKE_USER_DB = {
    "Goober@hmail.com" : {
        "email" : "Goober@gmail.com",
        "password" : "test",
        "account_type" : "buyer"
    }
}

@auth_router.get("/test")
def read_root():
    return {"auth": "test"}
    

@auth_router.post("/Register", response_model=AuthResponse)

    

def register_user(form: RegisterForm):


    found_user = FAKE_USER_DB.get(form.email)
    if(found_user):
        raise HTTPException(
            status_code=403,
            detail="user with this email alredy exists"
        )
    user_dict = form.model_dump()

    FAKE_USER_DB[form.email] = user_dict
    print("new user database")
    print(FAKE_USER_DB)

    return AuthResponse(
        email=form.email,
        account_type=form.account_type
    )

