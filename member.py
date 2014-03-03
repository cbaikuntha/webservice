from bottle import route,run,template,post,get,request,delete,put
mem_dict={}
details_list=[]
@post('/member/<idn>')
def addmember(idn):
	idn=request.POST['idn']
	name=request.POST['name']
	email=request.POST['email']
	info=','.join([name,email])
	mem_dict.update({idn:info})
	return mem_dict	
	
@get('/member/<idn>')
def memberdetails(idn):
	return template('<b> {{mem_dict[idn]}}',mem_dict=mem_dict,idn=idn)
	
@delete('/member/<idn>')
def delete_item(idn):
	if idn in mem_dict.keys():
		del(mem_dict[idn])
		return mem_dict
	else:
		return 'no record found'
		
@put('/member/<idn>')
def item_save(idn):
	if idn in mem_dict.keys():
		idn=request.POST['idn']
		name=request.POST['name']		
		email=request.POST['email']
		info=','.join([name,email])
		mem_dict.update({idn:info})
	return mem_dict
	
run(host='localhost',port=8086)

