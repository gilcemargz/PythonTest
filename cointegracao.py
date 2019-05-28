import pandas as pd
import numpy as np
from datetime import datetime
from MetaTrader5 import *
from pytz import timezone
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pytz
import statsmodels.tsa.stattools as smAdf
import time
import scipy.stats as scp


def carregaAtivos():
    papeis = ["PETR4","ABCB4","ABEV3","ALPA4","ALSC3","ALUP11","AMAR3","ANIM3","ARZZ3","AZUL4","B3SA3","BBDC3","BBDC4","BBSE3","BEEF3","BKBR3","BRAP4","BRDT3","BRFS3","BRKM5","BRML3","BRPR3","BRSR6","BTOW3","CAML3","CCRO3","CESP6","CIEL3","CMIG4","CPLE6","CSAN3","CSMG3","CSNA3","CVCB3","CYRE3","DIRR3","DMMO3","DTEX3","ECOR3","EGIE3","ELET3","ELET6","ELPL3","EMBR3","ENBR3","ENEV3","EQTL3","ESTC3","EVEN3","EZTC3","FESA4","FJTA4","FLRY3","GFSA3","GGBR4","GOAU4","GOLL4","GRND3","GUAR3","HGTX3","HYPE3","IGTA3","ITSA4","ITUB4","JBSS3","KLBN11","KROT3","LAME4","LEVE3","LIGT3","LINX3","LREN3","MEAL3","MGLU3","MOVI3","MRFG3","MRVE3","MULT3","MYPK3","NATU3","ODPV3","OMGE3","PARD3","PCAR4","PETR3","POMO4","PRIO3","QUAL3","RADL3","RAIL3","RAPT4","RENT3","RLOG3","SANB11","SAPR11","SAPR4","SBSP3","SEER3","SLCE3","SMLS3","SMTO3","STBP3","SULA11","SUZB3","TAEE11","TEND3","TGMA3","TIET11","TIMP3","TOTS3","TRPL4","TUPY3","UGPA3","UNIP6","USIM5","VALE3","VIVT4","VLID3","VULC3","VVAR3","WEGE3","BBAS3"]
    return papeis

ativosCoint = pd.DataFrame(columns=['DataInicio',
                                    'DataFinal',
                                    'Dependente',
                                    'Independente',
                                    'Periodo',
                                    'CoeficienteDepedente',
                                    'CoeficienteIndependente',
                                    'ValorDickey',
                                    'DesvioPadrao',
                                    'NivelConfianca'])

MT5Initialize()
MT5WaitForTerminal()

ativos = carregaAtivos()

timezone = pytz.timezone("Etc/UTC")
utc_from = datetime(2019, 1, 2, tzinfo=timezone)

"""
ratesDependente = MT5CopyRatesFrom('PETR4', MT5_TIMEFRAME_D1, utc_from, 100)
ratesIndependente = MT5CopyRatesFrom('PETR3', MT5_TIMEFRAME_D1, utc_from, 100)
frameDependente = pd.DataFrame(list(ratesDependente), columns=['time', 'open', 'low', 'high', 'close', 'tick_volume', 'spread', 'real_volume'])
frameIndependente = pd.DataFrame(list(ratesIndependente), columns=['time', 'open', 'low', 'high', 'close', 'tick_volume', 'spread', 'real_volume'])

print(len(frameDependente))
for x in ratesDependente:
    print(x)

#for index, row in frameDependente.iterrows():
#    print(row['open'])


precosDepe = frameDependente['close']
precosIndepe = frameIndependente['close']

X = precosIndepe
y = precosDepe
X = sm.add_constant(X)
results = sm.OLS(y, X).fit()
print(results.summary())

exit()
X = [5,12,25,35,45,55]
y = [5,20,14,32,22,38]
X = sm.add_constant(X)
results = sm.OLS(y, X).fit()
print(results.summary())

"""



antes = datetime.now()
ratesDependente = MT5CopyRatesFrom("PETR4", MT5_TIMEFRAME_D1, utc_from, 100 )

frameDependente = pd.DataFrame(list(ratesDependente),
                               columns=['time', 'open', 'low', 'high', 'close', 'tick_volume', 'spread',
                                        'real_volume'])

ratesIndependente = MT5CopyRatesFrom("PETR3", MT5_TIMEFRAME_D1, utc_from, 100)
frameIndependente = pd.DataFrame(list(ratesIndependente),
                                 columns=['time', 'open', 'low', 'high', 'close', 'tick_volume', 'spread',
                                          'real_volume'])

precosDepe = frameDependente['close']
precosIndepe = frameIndependente['close']






print(datetime.now()-antes)

X = precosIndepe
y = precosDepe
X = sm.add_constant(X)
results = sm.OLS(y, X).fit()
print(datetime.now()-antes)
print(results.summary())

result = scp.linregress( precosIndepe, precosDepe )

print(result)


print(results.params.const)
coef = results.params
print('coeficieine',coef.const)
print('close',coef.close)

residuos = results.resid
print('Desvio',np.std(residuos))

adf, pvalue, usedlag, nobs, critialvalues, icbest = smAdf.adfuller(residuos )
adfret = smAdf.adfuller(residuos )
print(adf)
print(pvalue)
print(usedlag)
print(nobs)
print(critialvalues)
print(icbest)
print(adfret)

df = pd.DataFrame(columns=['Periodo','Depe','Indepe'])
df = df.append({'Periodo':200,'Depe':'Petr3','Indepe':'Petr4'},ignore_index=True)
df = df.append({'Periodo':200,'Depe':'Petr3','Indepe':'Petr4'},ignore_index=True)
print(df)

print(datetime.now()-antes)

exit()


for x in range(100,80,-20):

    for simbDep in ativos:
        #print(at,x)
        antes = datetime.now()
        ratesDependente = MT5CopyRatesFrom(simbDep, MT5_TIMEFRAME_D1, utc_from, x )
        frameDependente = pd.DataFrame(list(ratesDependente),
                                       columns=['time', 'open', 'low', 'high', 'close', 'tick_volume', 'spread',
                                                'real_volume'])

        dataInicial = frameDependente['time'][0]
        dataFinal = frameDependente['time'][len(frameDependente) - 1]
        print(x, simbDep)
        for simbIndep in ativos:
            if(simbDep != simbIndep):
                print(x, simbDep, simbIndep,datetime.now() - antes)
                ratesIndependente = MT5CopyRatesFrom(simbIndep, MT5_TIMEFRAME_D1, utc_from, x)
                frameIndependente = pd.DataFrame(list(ratesIndependente),
                                                 columns=['time', 'open', 'low', 'high', 'close', 'tick_volume', 'spread',
                                                          'real_volume'])

                X = frameIndependente['close']
                y = frameDependente['close']

                result = scp.linregress(y, X)
                print(result)


"""                X = frameIndependente['close']
                y = frameDependente['close']
                X = sm.add_constant(X)
                results = sm.OLS(y, X).fit()

                adf, pvalue, usedlag, nobs, critialvalues, icbest = smAdf.adfuller(results.resid)

                if adf < 0.1:
                    ativosCoint = ativosCoint.append({'DataInicio':dataInicial,
                                                      'DataFinal':dataFinal,
                                                      'Dependente':simbDep,
                                                      'Independente':simbIndep,
                                                      'Periodo':x,
                                                      'CoeficienteDepedente':results.params.const,
                                                      'CoeficienteIndependente':results.params.close,
                                                      'ValorDickey':adf,
                                                      'DesvioPadrao':np.std(results.resid),
                                                      'NivelConfianca':99}, ignore_index=True)


"""


