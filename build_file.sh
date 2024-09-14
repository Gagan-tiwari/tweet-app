echo "BUILD START"
python3.9 -m venv .venv
source .venv/bin/activate
apt-get update && apt-get install -y python3-pip
pip install --upgrade pip
pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput
echo "BUILD END"