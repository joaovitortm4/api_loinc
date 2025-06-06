from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
import sqlite3

app = FastAPI()

class Dado(BaseModel):
    LOINC_NUM: Optional[str]
    COMPONENT: Optional[str]
    PROPERTY: Optional[str]
    TIME_ASPCT: Optional[str]
    SYSTEM: Optional[str]
    SCALE_TYP: Optional[str]
    METHOD_TYP: Optional[str]
    CLASS: Optional[str]
    CLASSTYPE: Optional[int]
    LONG_COMMON_NAME: Optional[str]
    SHORTNAME: Optional[str]
    EXTERNAL_COPYRIGHT_NOTICE: Optional[str]
    STATUS: Optional[str]
    VersionFirstReleased: Optional[str]
    VersionLastChanged: Optional[str]

@app.get("/dados", response_model=List[Dado])
def get_dados():
    conn = sqlite3.connect('banco_loinc.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            LOINC_NUM, COMPONENT, PROPERTY, TIME_ASPCT, SYSTEM, SCALE_TYP, METHOD_TYP, CLASS, 
            CLASSTYPE, LONG_COMMON_NAME, SHORTNAME, EXTERNAL_COPYRIGHT_NOTICE, STATUS, 
            VersionFirstReleased, VersionLastChanged
        FROM dados
    """)
    rows = cursor.fetchall()

    conn.close()

    return [
        {
            "LOINC_NUM": row[0],
            "COMPONENT": row[1],
            "PROPERTY": row[2],
            "TIME_ASPCT": row[3],
            "SYSTEM": row[4],
            "SCALE_TYP": row[5],
            "METHOD_TYP": row[6],
            "CLASS": row[7],
            "CLASSTYPE": row[8],
            "LONG_COMMON_NAME": row[9],
            "SHORTNAME": row[10],
            "EXTERNAL_COPYRIGHT_NOTICE": row[11],
            "STATUS": row[12],
            "VersionFirstReleased": row[13],
            "VersionLastChanged": row[14]
        }
        for row in rows
    ]
