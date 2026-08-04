from fastapi import FastAPI, APIRouter


def include_routers(
    *,
    app: FastAPI,
    routers_list: list[APIRouter],
) -> None:

    for router in routers_list:
        app.include_router(router=router)
