echo[$(date)]:"Start"
echo[$(date)]:"first create the env for conda"
conda create --prefix ./env python==3.11 -y

echo[$(date)]: "created teh environment"
echo[$(date)]:"now activate the environment with source command"
source activate ./env

echo[$(date)]:"end"