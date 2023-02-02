from Bio import Entrez

ids=""
def fasta_downloader():
    """
         Carga id_coati.txt en id_coatiy, descarga en formato genbank la información correspondiente a los identificadores de accesión usando el ENTREZ de Biopythony guarda en coati y en coati.gb
    """
    with open("data/coati.txt") as coati:
    name = coati.readline()[0:-1]
    for line in coati:
        ids += line.replace("\n","")
      

   
      


    
