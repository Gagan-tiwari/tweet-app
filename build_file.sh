echo "BUILD START"
python3.9 -m venv .venv
source .venv/bin/activate 
pip install --upgrade pip
pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput
echo "BUILD END"