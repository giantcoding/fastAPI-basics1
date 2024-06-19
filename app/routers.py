from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from .models import tasks, Task

router = APIRouter()



#FIXME: Sería interesante no incrustar en bruto el HTML para mejor práctica.
@router.get("/", response_class=HTMLResponse)
async def get_tasks(request: Request):
    task_cards = "".join(
        f'''
        <div class="col-md-4">
            <div class="card mb-4">
                <div class="card-body">
                    <h5 class="card-title">{task.title}</h5>
                    <p class="card-text">{task.description}</p>
                    <form action="/delete_task" method="post" style="display:inline;">
                        <input type="hidden" name="index" value="{i}">
                        <button type="submit" class="btn btn-danger">Delete</button>
                    </form>
                </div>
            </div>
        </div>
        ''' for i, task in enumerate(tasks)
    )
    with open("app/templates/index.html") as f:
        template = f.read()
    return HTMLResponse(template.format(tasks=task_cards))

@router.post("/", response_class=HTMLResponse)
async def add_task(request: Request, title: str = Form(...), description: str = Form(...)):
    tasks.append(Task(title, description))
    return RedirectResponse(url="/", status_code=303)

@router.post("/delete_task", response_class=HTMLResponse)
async def delete_task(request: Request, index: int = Form(...)):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return RedirectResponse(url="/", status_code=303)
