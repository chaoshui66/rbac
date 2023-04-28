from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter()


class CreateRegionReq(BaseModel):
    name: str


@router.post("/region")
async def create_region(body: CreateRegionReq):
    return body


@router.get("/region")
async def get_region_list():
    return {}


@router.get("/region/{region_id}")
async def get_region_detail():
    return {}


@router.patch("/region/{region_id}")
async def update_region_name():
    return {}


@router.delete("/region/{region_id}")
async def delete_region():
    return {}
