from DBConnection import DBConnection
from StringCompare import StringCompare

class  AverageContentSimilarity:

	def main(uid, product):
		res="Non Spam";
		database = DBConnection.getConnection()
		cursor = database.cursor()
		sql="select review from reviews where user=%s and product=%s ";
		values(uid,product)
		cursor.execute(sql,values)
		rows = cursor.fetchall()

		d1=0.0;
		d2=0.0;
		v=[]
		for row in rows:
			v.append(row[0]);
			
		
		if len(v)>0:
			for x in range(len(v)):
				try:
					d2=StringCompare.do(v[0],v[x+1]);
					if d2>d1:
						d1=d2;
				except Exception as e:
					pass
				
			
		if d1>50:
			res="Spam";
		else:
			res="Non Spam";
		return res;


		
	def process():
		database = DBConnection.getConnection()
		cursor = database.cursor()
		sql="select * from REVIEWs";
		cursor.execute(sql)
		rows = cursor.fetchall()
		for row in rows:
			r=AverageContentSimilarity.main(row[5],row[1])
			#print(r)
			if r=='Spam':
				sql="update reviews set spam='"+str(r)+"' where rid='"+str(row[0])+"' and spam='Non Spam' ";
				cursor.execute(sql)
				database.commit()

#AverageContentSimilarity.process()