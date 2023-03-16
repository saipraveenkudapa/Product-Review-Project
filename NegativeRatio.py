from DBConnection import DBConnection

class  NegativeRatio:
	def main(uid, product):
		res="Non Spam";
		database = DBConnection.getConnection()
		cursor = database.cursor()
		
		sql="select avg(rating), count(*) from reviews  where user=%s and product=%s ";
		values=(uid,product)
		cursor.execute(sql,values)
		rows = cursor.fetchall()
		d1=0.0;
		for row in rows:
			d1=row[0]
			records=row[1]
		if records>1:
			if(d1>2.0):
				res="Non Spam";
			else:
				res="Spam";
		else:
			res="Non Spam"
		return res
	def process():
		database = DBConnection.getConnection()
		cursor = database.cursor()
		sql="select * from REVIEWs";
		cursor.execute(sql)
		rows = cursor.fetchall()
		for row in rows:
			r=NegativeRatio.main(row[5],row[1])
			print(r)
			if r=='Spam':
				sql="update reviews set spam='"+str(r)+"' where rid='"+str(row[0])+"' and spam='Non Spam' ";
				cursor.execute(sql)
				database.commit()

NegativeRatio.process()