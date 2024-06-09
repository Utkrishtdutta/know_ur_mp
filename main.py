from fastapi import FastAPI
import pandas as pd

app = FastAPI()


@app.get('/{constituency}')
async def know_ur_mp(constituency):
    try:
        constituency = constituency.upper()
        df = pd.read_csv('election_results_2024.csv')
        mp = df.loc[df['Constituency']==constituency, ['Leading Candidate','Leading Party']]
        if mp.empty:
            return {"Error":"Select right constituency"}
        return {f'The elected member of parliament from {constituency}': f'{mp["Leading Candidate"].values[0]} ({mp["Leading Party"].values[0]})'}
    except Exception as e:
        return {"Error" : str(e)}
