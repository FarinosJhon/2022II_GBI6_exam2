##EJERCICIO 3
#Función 1. Fasta downloader.
from Bio import Entrez 
from Bio import SeqIO 

def fasta_downloader():
    """
         Carga id_coati.txt en id_coatiy, descarga en formato genbank la información correspondiente a los identificadores de accesión usando el ENTREZ de Biopythony guarda en coati y en coati.gb
    """
# abrimos el archivo txt
my_file = open("data/coati.txt", "r")
  
# Leemos el archivo
data = my_file.read()
  
# Creamos una lista donde cada objeto se añade después de un salto \n
coati_list = data.split("\n")
my_file.close()
      
#Descargamos los datos de NCBI con ENTREZ. 
id_list = coati_list
Entrez.email = "jhonmarco630@gmail.com" 
coati = []
with Entrez.efetch( db="nucleotide", rettype="gb", retmode="text", id= id_list
                  ) as handle: 
      for seq_record in SeqIO.parse(handle, "gb"): 
        coati.append(seq_record)
        SeqIO.write(coati, "coati.gb", "genbank")  

#################################################################
#Función 2. Alineamiento de secuencias
from Bio.Align.Applications import ClustalwCommandline
import os

def alignment():
    """
     Sirve para extraer únicamente las secuencias de la variable coati y realiza un alineamiento usando clustalW.
    """
    

    
