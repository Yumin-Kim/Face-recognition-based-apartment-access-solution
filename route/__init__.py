# route 폴더에 있지만 /route/__init__.py가 실행되는 시점은 메인 폴더에서 실행되기 때문에
# route안에 있는 todo를 사용하게다고 정의가 따로 필요
from route.todo import Todo
from route.admin import Admin
from route.face import Face

