import pandas as pd
import os
import dotenv
from dotenv import load_dotenv

load_dotenv()

FBEXPORT = os.getenv('FBEXPORT')
SVENSKALAG = os.getenv('SVENSKALAG')

fb = pd.read_csv(FBEXPORT)
svenskalag = pd.read_excel(SVENSKALAG)

fbfullname = fb['Full Name']
svenskalagfornamn = svenskalag['Förnamn']
svenskalagefternamn = svenskalag['Efternamn']
svenskalagkomplett = svenskalagfornamn + ' ' + svenskalagefternamn
svenskalagkomplett = svenskalagkomplett.rename('Full Name')
svenskalagkomplett = svenskalagkomplett.str.lower()
fbfullname = fbfullname.str.lower()


comparison_result = pd.merge(fbfullname, svenskalagkomplett, how='left', indicator=True)
comparison_result = comparison_result.loc[comparison_result['_merge'] == 'left_only']
print(comparison_result)