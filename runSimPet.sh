#set -x
#SCRIPT PARA AUXILIAR NA EXECUCAO DE PROGRAMAS 
# DE SIMULACAO DE ESCOAMENTOS EM RESERVATORIOS 
#
#
#AUTORES: bidu@lncc.br e tuane@lncc.br
# Alterado por Diego para casos de arquivos comprimidos.
# 06.2013
# 11.2015
#
# foma de utilizacao . rodarSimulador.sh exp10x10x30

#### EXPERIMENTOS ####

# diretorio do experimento:
# dirPadrao ou lido de primeiro argumento da linha de comando
dirPadrao=teste
dirExp="$(pwd)"/${1:-${dirPadrao}} 

#rm -rf ${dirExp}/out/*.vtk
rm -rf ${dirExp}/echo.*
rm -rf ${dirExp}/fort.*
rm -rf ${dirExp}/tela*
rm -rf ${dirExp}/coordenadas.dat
rm -rf ${dirExp}/conectsLadais.dat
rm -rf ${dirExp}/conectsNodais.dat
rm -rf ${dirExp}/velocidadeLadal_RT.txt
rm -rf ${dirExp}/pressao_RT.txt

arqTela=${dirExp}/tela.txt

#### DEFINICAO DO NUMERO DE THREADS (OPENMP) E PROCESSOS (MPI) ####
ntPadrao=1
numThreads=${2:-${ntPadrao}}
export OMP_NUM_THREADS=${numThreads}


npPadrao=1
#numProcs=${3:-${npPadrao}}
numProcs=${npPadrao}
export NP=${numProcs} # atribuir valor padrao aa variavel NP

#ARGSP=" "
#echo "${ARGSP}"

#### DEFINICAO DO EXECUTAVEL ####
DIRBIN=$(pwd)  #"/prj/prjedlg/tuane/Siger/simuladorGeocreep/bin"
DIRBIN=${3:-"./bin/"}


LOCAL=$(pwd)
NOMEEXECUTAVEL=simulador.exe

#cd ..
#DIRBIN="$(pwd)/bin"  

#cd ${LOCAL}

EXECUTAVEL=$LOCAL/${DIRBIN}/${NOMEEXECUTAVEL}

#### definicao do comando a ser executado
comando="(export  OMP_NUM_THREADS=${numThreads} ; cd ${dirExp}; time  ${EXECUTAVEL})"

if [ -e ${EXECUTAVEL} ] 
then
  printf "\n diretorio do experimento.: %s\n" ${dirExp}  
  printf "\n nome do executavel.......: %s\n" ${EXECUTAVEL} 
  printf "\n numero de threads .......: %d\n" ${OMP_NUM_THREADS}
  printf "\n numero de processos......: %d\n" ${NP}
  printf "\n comando .................: %s\n" "${comando}"
  eval ${comando}  |tee  ${arqTela}
  tar cfz "${1}.tar.gz" ${1}
  rm -rf ${dirExp}/*.0
  rm -rf ${dirExp}/*.1
  rm -rf ${dirExp}/*.2
  rm -rf ${dirExp}/*.3
  rm -rf ${dirExp}/*.4
  rm -rf ${dirExp}/*.5
  rm -rf ${dirExp}/*.6
  rm -rf ${dirExp}/*.7
  rm -rf ${dirExp}/*.8
  rm -rf ${dirExp}/*.9
else
  printf "\n EXECUTAVEL NAO ENCONTRADO \n"
  printf "\n comando .................: %s\n" "${comando}"
fi
