from pylab import * # plots etc
import scipy.signal as signal # design the filter fir
import json # Read Json files
import webbrowser # Open a web browser in a specific link
import os # list archives in a specific directory

"""
Elabore uma interface gráfica para projeto de filtros FIR por janelamento em geral. A
interface deverá permitir ao usuário a inserção/seleção dos seguintes parâmetros: (3,0)
a) Tipo de Filtro: passa-baixas, passa-altas, passa-faixas, rejeita-faixas;
b) Frequências de Corte: para filtros passa-baixas e passa-altas (FC1 e FC2); filtros passa-faixa e
rejeita faixa (FC1, FC2, FS1, FS2);
c) Frequência de Amostragem;
d) Atenuação mínima na faixa de rejeição (-21 dB, -25 dB, -44 dB, -53 dB, -74 dB)
A partir dos parâmetros inseridos, a interface deverá apresentar ao usuário:
 - Resposta em frequência do filtro (Decibéis x Frequência);
 - Número de coeficientes do filtro.
"""
#Plot frequency and phase response
def mfreqz(b,a=1):
    f = np.arange(0, (fs / 2) - 1 + 1)  # + 1 para variar de 0 até (Fs/2 - 1)
    w, h = signal.freqz(b,a,worN=f,fs=fs)  # worN: compute the response at the frequencies given. These are in the same units as fs.
    h_dB = 20 * log10(abs(h))
    plot(f,h_dB)
    ylim(-150, 10)
    ylabel('Magnitude (db)')
    xlabel(r'Frequency (Hz)')
    title('Magnitude response in dB\nNumber of coefficients: {}'.format(n))

#Calculate coefficients
def coeff(wt):
    M= (dtt*pi)/wt
    M = round(M + 0.5)
    return (M)

#Filter attenuation
def attenuation(att):
    if att == 1:
        window = "boxcar"
    elif att == 2:
        window = "bartlett"
    elif att == 3:
        window = "hanning"
    elif att == 4:
        window = "hamming"
    elif att == 5:
        window = "blackman"
    return(window)

def coeffatt(att):
    if att == 1:
        dtt = 1.8
    elif att == 2:
        dtt = 6.1
    elif att == 3:
        dtt = 6.2
    elif att == 4:
        dtt = 6.6
    elif att == 5:
        dtt = 11
    return(dtt)

#Filter
def firwin(filter):
    if filter == 1:
        # Low pass filter
        a = signal.firwin(n, cutoff=fc, window=window, fs=fs)
        # Frequency response
        mfreqz(a)
        show()
    elif filter == 2:
        # High pass filter
        a = signal.firwin(n, cutoff=fc, window=window, fs=fs, pass_zero=False)
        # Frequency response
        mfreqz(a)
        show()
    elif filter == 3:
        # Band pass filter
        a = signal.firwin(n, cutoff=[fc1, fc2], window=window, fs=fs, pass_zero=False)
        # Frequency response
        mfreqz(a)
        show()
    elif filter == 4:
        # Band pass filter
        a = signal.firwin(n, cutoff=[fc1, fc2], window=window, fs=fs)
        # Frequency response
        mfreqz(a)
        show()

# wait for the user inputs until he confirm
def waitUntilConfirm(jsonPath):

    bSolicitou = False    

    while (bSolicitou == False): # While user doesn't confirm:

        for file in os.listdir(jsonPath): # For each archive inside the jsonPath:

            if file.endswith('.json'): # If the file ends with json format:

                bSolicitou = True # Means that the user has confirmed the parameters

                return True # Break the function

            else:

                bSolicitou = False # Remains false then check again.

def getFilterParameters(jsonPath):

    f = open(jsonPath,'r')

    parameters = json.load(f) 

    return parameters


# = = = = = = = = = = Main Function = = = = = = = = = = #

# Path to the json archive with the filter parameters
MyJsonFolder = '/home/trs/Iot_Projects/PDS_FilterFir/LowPassFIRFilter/temp'
MyJsonPath = '/home/trs/Iot_Projects/PDS_FilterFir/LowPassFIRFilter/temp/temp.json'

# After the plot and print, delete the json archive.
os.remove(MyJsonPath)

# Open the node-red web page at the user interface
webbrowser.open('http://127.0.0.1:1880/ui/#!/0?socketid=vBwc0gNyW5awp8SYAAAQ', new = 2)

confirmed = waitUntilConfirm(MyJsonFolder)

if (confirmed): # if the user has confirmed the filter parameters:

    # Here parameters is a dictionary
    parameters = getFilterParameters(MyJsonPath)

    # Untangle the dic filter parameters 
    filter = int(parameters["filter_type"])

    if ((filter == 1) or (filter == 2)):
        fc1 = (parameters["cut_off1"])

        fc2 = (parameters["cut_off2"])

        fs = (parameters["fs"])

        att = (parameters["att"])

        wc1 = (fc1/(fs/2))*pi

        wc2 = (fc2/(fs/2))*pi

        fc = (fc2 + fc1) / 2

        wt = wc2 - wc1  # Length of frequency response.

    elif ((filter == 3) or (filter == 4)):
        fci1 = (parameters["cut_off1"])

        fci2 = (parameters["cut_off2"])

        fcs1 = (parameters["cut_off_sup1"])

        fcs2 = (parameters["cut_off_sup2"])

        fs = (parameters["fs"])

        att = (parameters["att"])

        wci1 = (fci1/(fs/2))*pi

        wci2 = (fci2/(fs/2))*pi

        wcs1 = (fcs1/(fs/2))*pi

        wcs2 = (fcs2/(fs/2))*pi

        fc1 = ((fci2 + fci1)/2)

        fc2 = ((fcs2 + fcs1)/2)

        wt = min((wci2 - wci1),(wcs2 - wcs1))  # Length of frequency response.

    # Return the appropriate window according the attenuation inputed
    window = attenuation(att)

    dtt = coeffatt(att)

    n = coeff(wt)

    firwin(filter)

    print('the number of coefficients is ',n)

    



