from ninja import Schema
from typing import Optional
from datetime import datetime

from django.contrib.auth.models import User

class UserOut(Schema):
    id: int
    email: str
    first_name: str
    last_name: str


class CourseSchemaOut(Schema):
    id: int
    name: str
    description: str
    price: int
    image : Optional[str]
    teacher: UserOut
    created_at: datetime
    updated_at: datetime

class CourseMemberOut(Schema):
    id: int 
    course_id: CourseSchemaOut
    roles: str
    created_at: datetime


class CourseSchemaIn(Schema):
    name: str
    description: str
    price: int


class CourseContentMini(Schema):
    id: int
    name: str
    description: str
    course_id: int
    created_at: datetime
    updated_at: datetime


class CourseContentFull(Schema):
    id: int
    name: str
    description: str
    video_url: Optional[str]
    file_attachment: Optional[str]
    course_id: int
    created_at: datetime
    updated_at: datetime

class CourseCommentOut(Schema):
    id: int
    content_id: int
    user_id: UserOut
    created_at: datetime
    updated_at: datetime

class CourseCommentIn(Schema):
    content_id: int
    user_id: int
    comment: str
