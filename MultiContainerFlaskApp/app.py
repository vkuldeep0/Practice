from flask import Flask
import redis
import psycopg2
import os


# Create a Flask app instanc
app = Flask(__name__)

# Redis connection
redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = 6379
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

# PostgrepSQL connection
db_host = os.getenv("DB_HOST", "db")
db_name = os.getenv("POSTGRES_DB", "postgres")
db_user = os.getenv("POSTGRES_USER", "postgres")
db_pass = os.getenv("POSTGRES_PASSWORD", "postgres")

# Define a route (URL endpoint)
@app.route("/")
def home():
	# Test Redis
	r.set("message", "Hello from Redis!")
	redis_msg = r.get("message")

	# Test Postgres
	conn = psycopg2.connect(
		host=db_host,
		database=db_name,
		user=db_user,
		password=db_pass
	)
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS visits (id SERIAL PRIMARY KEY, message TEXT);")
	cur.execute("INSERT INTO visits (message) VALUES ('Hello from Postgres!');")
	conn.commit()
	cur.execute("SELECT COUNT(*) FROM visits;")
	count = cur.fetchone()[0]
	cur.close()
	conn.close()

	return f"""
	<h1>Flask is running! </h1>
	<p>Redis says: {redis_msg}</p>
	<p>Postgres total visits: {count}</p>
	"""

# Run the app
if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000, debug=True)
