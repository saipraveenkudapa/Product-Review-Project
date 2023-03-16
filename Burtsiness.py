from DateDiff import DateDiff
from DBConnection import DBConnection
class  Burstiness:
	def main(uid, product):
		res="Non Spam";
		try:
		        database = DBConnection.getConnection()
		       	cursor = database.cursor()
		       	sql="select max(date_), min(date_), count(*) from REVIEWs where user=%s and product=%s ";
		       	values=(uid,product)
		       	cursor.execute(sql,values)
		
        		
        		for row in rows:
        			last=row[0]
        			first=row[1]
        			records=row[2]
        		if records>1:
        			d1=abs(DateDiff.numOfDays(last,first));
        			print(last+"	"+first+"	Diff="+str(d1));
        			d1=d1/28;
        			d1=1-d1;
        			if d1>0.5:
        				res="Spam";
        			else:
        				res="Non Spam";
        		else:
        			res="Non Spam";
				

		
		except Exception as e:
			print(e)
		return res


	def process():
		database = DBConnection.getConnection()
		cursor = database.cursor()
		sql="select * from REVIEWs";
		cursor.execute(sql)
		rows = cursor.fetchall()
		for row in rows:
			r=Burstiness.main(row[5],row[1])
			print(r)
			sql="update reviews set spam='"+str(r)+"' where rid='"+str(row[0])+"' ";
			cursor.execute(sql)
			database.commit()






#Burstiness.process()

