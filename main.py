from fastapi import FastAPI, File, Form
from fastapi.middleware.cors import CORSMiddleware
from datetime import date
import json

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def load_json():
    with open("./website.json","r") as f:
        jsonFile=json.load(f)
    return jsonFile


@app.post('/')
def rootPage():
    return ('Welcome to my first First API project')

@app.post("/achievements/")
async def upload_achievements(header:str=Form(...),description: str = Form(...), image: str = Form(...),url:str=Form(...)):
    # with open(f"./assets/achievements/{image.filename}", "wb") as f:
    #     f.write(image.file.read())
    # path=os.path.join("assets","achievements",image.filename)
    dat=str(date.today())
    jsonFile=await load_json()
    jsonFile['achievements'].append(
        {'file': image,'header':header, 'description': description,'url':url,'date':dat
    })
    with open('./website.json',"w") as f:
        json.dump(jsonFile,f)

    return jsonFile


@app.post("/projects/")
async def upload_projects(header:str=Form(),description: str = Form(...), image: str = Form(...), url: str = Form(...)):
    # with open(f"./assets/projects/{image.filename}", "wb") as f:
    #     f.write(image.file.read())
    # path = os.path.join("assets", "projects", image.filename)
    dat = str(date.today())
    jsonFile = await load_json()
    jsonFile['projects'].append(
        {'file': image,'header':header, 'description': description, 'url': url, 'date': dat
        })
    with open('./website.json', "w") as f:
        json.dump(jsonFile, f)

    return jsonFile


@app.post("/skills/")
async def upload_skills(percentage:float=Form(...),name: str = Form(...), image: str = Form(...), url: str = Form(...)):
    # with open(f"./assets/skills/{image.filename}", "wb") as f:
    #     f.write(image.file.read())
    # path = os.path.join("assets", "skills", image.filename)
    jsonFile = await load_json()
    jsonFile['skills'].append(
        {'file': image, 'name': name,'percentage':percentage,'url': url})
    with open('./website.json', "w") as f:
        json.dump(jsonFile, f)

    return jsonFile

@app.post("/events/")
async def upload_events(description: str = Form(...), organization:str=Form(...),image: str = format(...),url:str=Form(...)):
    # with open(f"./assets/events/{image.filename}", "wb") as f:
    #     f.write(image.file.read())
    # path=os.path.join("assets","events",image.filename)
    dat=str(date.today())
    jsonFile=await load_json()
    jsonFile['events'].append(
        {'file': image, 'organization': organization, 'description': description, 'url': url, 'date': dat
    })
    with open('./website.json',"w") as f:
        json.dump(jsonFile,f)

    return jsonFile


# @app.get("/getimage/{prompt}/{filename}")
# async def get_image(prompt: str,filename: str):
#     file_path = os.path.join('assets',prompt, filename)
#     return FileResponse(file_path)

@app.get("/content/{prompt}")
async def get_content(prompt:str):
    jsonResponse=await load_json()
    return jsonResponse[prompt]

@app.get("/delete/{prompt}/{id}")
async def delete_content(prompt:str,id:int):
    jsonResponse=await load_json()

    # try:
    #     os.remove(os.path.join(jsonResponse[prompt][id]['file']))
    # except Exception as e:
    #     pass
    try:
        del jsonResponse[prompt][id]
        with open('./website.json',"w") as f:
            json.dump(jsonResponse,f)
            return {"status":"success"}
    except Exception as e:
        return {"status":"failed"}
    
        