db_session = scoped_session(
  sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
  )
)
# DBにあるWineのデータを全件取得
db = db_session.query(Wine).all()
for row in db:
  # カラムを指定してデータを取得する
  print(row.alcohol)