def fasta_downloader(coati):
    """
         Carga id_coati.txt en id_coatiy, descarga en formato genbank la información correspondiente a los identificadores de accesión usando el ENTREZ de Biopythony guarda en coati y en coati.gb
    """
    from Bio import Entrez
   
    ids = []
    with open("data/coati.txt", 'r+') as coati:
    coati = coati.read()
    line =  coati.split("\n")[0:]
   
      


    
