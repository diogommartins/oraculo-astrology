from typing import Union
from uuid import uuid4

from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, Field
import uvicorn
from backend.astrological_subject import AstrologicalSubject
from backend.charts.kerykeion_chart_svg import Chart

app = FastAPI()


class Subject(BaseModel):
    city: str
    year: int
    month: int
    day: int
    hour: int = 12
    minute: int = 0
    lat: float = -22.922771544773106
    lng: float = -42.81663370244884
    name: str =  "Desconhecido"
    tz_str: str = "America/Sao_Paulo"
    entity_id: str = Field(default_factory=lambda: uuid4().hex)


@app.get("/")
def read_root():
    return RedirectResponse("/docs")


@app.post("/subject")
def create_subject(subject: Subject):
    astro =  AstrologicalSubject(
        name=subject.name, 
        year=subject.year,
        month=subject.month,
        day=subject.day,
        hour=subject.hour,
        minute=subject.minute,
        lat=subject.lat,
        lng=subject.lng,
        tz_str=subject.tz_str,
        city=subject.city
    )

    chart = Chart(astro)
    chart.makeSVG()
    return Response(content=chart.template, media_type="image/svg+xml")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)