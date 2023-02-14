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
        SeqIO.write(coati, "data/coati.gb", "genbank")  

#################################################################
#Función 2. Alineamiento de secuencias
from Bio import SeqIO
from Bio import AlignIO
from Bio import Phylo
from Bio.Align.Applications import ClustalwCommandline
import os

def alignment():
    """
     Sirve para extraer únicamente las secuencias de la variable coati y realiza un alineamiento usando clustalW.
    """
    ella = SeqIO.parse("data/coati.gb", "genbank")
    yo = SeqIO.write(ella, "data/coati.fasta", "fasta")
    
    clustalw_exe = r"C:\Program Files (x86)\ClustalW2\clustalw2.exe"
    clustalw_cline = ClustalwCommandline(clustalw_exe, infile = "data/coati.fasta")
    assert os.path.isfile(clustalw_exe), "Clustal_W executable is missing or not found"
    stdout, stderr = clustalw_cline()
     
    with open("data/coati.aln", "r") as jhon:    
        ClustalAlign = AlignIO.read(jhon, "clustal")

    return["Aligned"]
    
##################################################################
#Función 3. Árbol filogenético

def tree():
    """
    Realiza el cálculo de las distancias utilizando coati.aln y finalmente que imprime en la pantalla el árbol filogenético y lo guarda en data como coati_phylotree.pdf
    """
    from Bio import AlignIO
    from Bio import Phylo 
    from Bio.Phylo.TreeConstruction import DistanceCalculator 
    
    calculator = DistanceCalculator('identity')
    
    from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
    
    constructor = DistanceTreeConstructor(calculator)
    with open("data/coati.aln", "r") as alin: 
        alignment = AlignIO.read(alin, "clustal")
    
    distance_matrix = calculator.get_distance(alignment)
    
    arbolito = constructor.build_tree(alignment)
    arbolito.rooted = True
    
    Phylo.write(arbolito, "data/coati_phylotree.pdf", "phyloxml")
    Phylo.read(file="data/coati_phylotree.pdf", format="phyloxml")
    
    Phylo.draw(arbolito)
    
    return[arbolito]
    
    