_N='family'
_M='/Patient/'
_L='Organization'
_K='name'
_J='FirstName_'
_I='LastName_'
_H='Patient'
_G=True
_F='⚠ unexpected result'
_E='\n'
_D='✓ success!'
_C=False
_B=None
_A=' '
import sys,os, json
dpath=os.path.dirname(__file__)
import socket,urllib.parse,contextlib
from io import StringIO
@contextlib.contextmanager
def nostdout():A=sys.stdout;sys.stdout=StringIO();yield;sys.stdout=A
def checkPortOpen(url):
	C='Cannot connect to server.';A=urllib.parse.urlparse(url);D={'http':80,'https':443}.get(A.scheme,80)if A.port is _B else A.port;E=A.hostname
	try:B=socket.socket(socket.AF_INET,socket.SOCK_STREAM);F=B.connect_ex((E,D));B.close();return F==0,C
	except:return _C,C
def checkEx_0():print('Check 0 - Testserver');print(2*_A+'-Testserver is running?');from Day7.ex_00_settings import HTTP_TEST_ENDPOINT as A;B,C=checkPortOpen(A);print(4 * _A + (_D if B else '⚠ Not running: ' + C) + _E)
def checkEx_1():
	G='text';F='FHIR';E='info';print('Check 1 - HTTP');print(2*_A+'-GET Request');from Day7.ex_00_settings import HTTP_TEST_ENDPOINT as B;from ex_01_http import sendGETRequest as H
	try:C,D=H(B+'/get');A=json.loads(C)[E]==F and D==200
	except Exception as I:print(I);A=_C
	print(4*_A+(_D if A else'⚠ GET request failed')+_E);print(2*_A+'-POST Request');from Day7.ex_00_settings import HTTP_TEST_ENDPOINT as B;from ex_01_http import sendPOSTRequest as J
	try:C,D=J(B+'/post',json.dumps({G:'Hallo!'}));A=json.loads(C)[G]=='!ollaH'and D==200
	except:A=_C
	print(4*_A+(_D if A else'⚠ POST request failed')+_E);print(2*_A+'-DELETE Request');from Day7.ex_00_settings import HTTP_TEST_ENDPOINT as B;from ex_01_http import sendDELETERequest as K
	try:C,D=K(B+'/delete');A=json.loads(C)[E]==F and D==200
	except:A=_C
	print(4*_A+(_D if A else'⚠ DELETE request failed')+_E)
def checkEx_2():
	print('Check 2 - FHIR (First Steps)');print(2*_A+'-Family name of Patient ID 1');from Day7.ex_00_settings import FHIR_API_ENDPOINT as B;from ex_01_http import sendGETRequest as C;from ex_02_fhir_firststeps import demo_patient_id as E
	try:
		with nostdout():F=E()
		D=json.loads(C(B+_M+'1')[0]).get(_K)[0].get(_N);A=F==D
	except:A=_C
	print(4*_A+(_D if A else _F)+_E);print(2*_A+'-Count patients');from Day7.ex_00_settings import FHIR_API_ENDPOINT as B;from ex_01_http import sendGETRequest as C;from ex_02_fhir_firststeps import demo_count_patients as G
	try:
		with nostdout():H=int(G())
		I=int(json.loads(C(B+'/Patient?_total=accurate')[0]).get('total'));A=I==H
	except:A=_C
	print(4*_A+(_D if A else _F)+_E);print(2*_A+'-Load patient from server');
    from ex_02_fhir_firststeps import demo_fhir_patient as J
	try:
		with nostdout():K=J()
		A=K.name[0].family==D
	except:A=_C
	print(4*_A+(_D if A else _F)+_E)
def checkEx_3():
	print('Check 3 - Resources');print(2*_A+'-Upload Resource');
    from ex_03_fhir import uploadResource as H;from fhir.resources.patient import Patient as C;from fhir.resources.humanname import HumanName as K;import uuid as E
	try:I=_I+str(E.uuid4());J=_J+str(E.uuid4());F=C();B=K();B.family=I;B.given=[J];F.name=[B];G=H(F);L=json.loads(G);A=L.get(_K,[{}])[0].get(_N,'')==I and L.get(_K,[{}])[0].get('given',[''])[0]==J;P=L['id'];from Day7.ex_00_settings import FHIR_API_ENDPOINT as D;from ex_01_http import sendDELETERequest as Q;Q(D + _M + str(P))
	except:A=_C
	print(4*_A+(_D if A else _F)+_E);print(2*_A+'-Load Resources');
    from ex_03_fhir import loadResources as N;
    try:
		def O(filter):
			I=_H;J=C;B=[];E=D+'/'+I
			if filter:E+='?identifier=submitter|'+RZ_KENNUNG
			A=E
			while A is not _B:
				K,P=M(A);F=json.loads(K)
				for L in F.get('entry',[]):
					G=L.get('resource',_B)
					if G is not _B:N=J(**G);B.append(N)
				O=F.get('link',[]);A=_B
				for H in O:
					if H['relation']=='next':A=H['url']
			return B
		A=N(_H,filter=_G)==O(filter=_G)and N(_H,filter=_C)==O(filter=_C)
	except:A=_C
	print(4*_A+(_D if A else _F)+_E);print(2*_A+'-Delete Resource');from Day7.ex_00_settings import FHIR_API_ENDPOINT as D,RZ_KENNUNG;from ex_01_http import sendGETRequest as M;from ex_03_fhir import uploadResource as H,deleteResource as R;from fhir.resources.patient import Patient as C;from fhir.resources.humanname import HumanName as K;import uuid as E
	try:I=_I+str(E.uuid4());J=_J+str(E.uuid4());F=C();B=K();B.family=I;B.given=[J];F.name=[B];G=H(F);S=C.parse_raw(G);G=R(S);A='Successfully deleted'in G
	except:A=_C
	print(4*_A+(_D if A else _F)+_E)
def checkEx_4():
	print('Check 4 - Statistics');print(2*_A+'-Compute average age');
    from ex_04_fhir_simple_statistics import computeAgeAverage as C;
    try:
		def E(filter):
			C=B(_H,filter=filter);A=[];E=date.today()
			for F in C:G=D(E,F.birthDate).years;A.append(G)
			if len(A)>0:return sum(A)/len(A)
			return-1
		A=C(_G)==E(_G)and C(_C)==E(_C)
	except:A=_C
	print(4*_A+(_D if A else _F)+_E);print(2*_A+'-Compute deceased percentage');
    from ex_03_fhir import loadResources as B;from ex_04_fhir_simple_statistics import computeDeceasedPercentage as F;
    from datetime import date;from dateutil.relativedelta import relativedelta as D
	try:
		def G(filter):
			A=B(_H,filter=filter);D=0
			for C in A:
				E=(C.deceasedBoolean is _B or not C.deceasedBoolean)and C.deceasedDateTime is _B
				if not E:D+=1
			if len(A)>0:return D/len(A)
			else:return-1
		A=F(_G)==G(_G)and F(_C)==G(_C)
	except:A=_C
	print(4*_A+(_D if A else _F)+_E)
def checkEx_5():
	X='Org_';print('Check 5 - Custom FHIR objects');print(2*_A+'-Create custom patient');from fhir.resources.patient import Patient as H;from fhir.resources.humanname import HumanName as K;from fhir.resources.address import Address;from datetime import date;from ex_05_fhir_create_custom import createCustomPatient as Y
	try:B=H();C=K();C.family='Meyer';C.given=['Maximilian'];B.name=[C];I=Address();I.line=['Salomon-Idler-Straße 4'];I.postalCode='86159';I.city='Augsburg';I.state='Bayern';I.country='Deutschland';B.address=[I];B.birthDate=date(year=2000,month=1,day=1);B.deceasedBoolean=_C;B.gender='male';Z=Y();A=Z==B
	except:A=_C
	print(4*_A+(_D if A else _F)+_E);print(2*_A+'-Create custom organization');from fhir.resources.organization import Organization as J;
    from ex_05_fhir_create_custom import createCustomOrganization as a
	try:D=J();D.name='Universitätsklinikum Augsburg';b=a();A=b==D
	except:A=_C
	print(4*_A+(_D if A else _F)+_E);print(2*_A+'-Lookup patient');from ex_03_fhir import deleteResource as E,uploadResource as L;from fhir.resources.patient import Patient as H;from fhir.resources.humanname import HumanName as K;
    from ex_05_fhir_create_custom import lookupCustomPatientOnServer as T;import uuid
	try:
		Q=_I+str(uuid.uuid4());R=_J+str(uuid.uuid4());B=H();C=K();C.family=Q;C.given=[R];B.name=[C];M=T(B);A=M is _B
		if A:
			c=L(B);e=H.parse_raw(c);M=T(B);A=M is not _B
			if M is not _B:E(M)
	except:A=_C
	print(4*_A+(_D if A else _F)+_E);print(2*_A+'-Lookup organization');from ex_03_fhir import deleteResource as E,uploadResource as L;from fhir.resources.organization import Organization as J;
    from ex_05_fhir_create_custom import lookupCustomOrganizationOnServer as U;import uuid
	try:
		S=X+str(uuid.uuid4());D=J();D.name=S;N=U(D);A=N is _B
		if A:
			d=L(D);f=J.parse_raw(d);N=U(D);A=N is not _B
			if N is not _B:E(N)
	except:A=_C
	print(4*_A+(_D if A else _F)+_E);print(2*_A+'-Retrieve patient');from ex_03_fhir import deleteResource as E;from fhir.resources.patient import Patient as H;from fhir.resources.humanname import HumanName as K;from ex_05_fhir_create_custom import createOrRetrievePatientOnServer as V;import uuid
	try:
		Q=_I+str(uuid.uuid4());R=_J+str(uuid.uuid4());B=H();C=K();C.family=Q;C.given=[R];B.name=[C];F=V(B);A=F is not _B
		if A:
			O=V(B);A=F is not _B and F.id==O.id
			if F.id!=O.id:
				if F.id is not _B:E(F)
				if O.id is not _B:E(O)
			else:E(F)
	except:A=_C
	print(4*_A+(_D if A else _F)+_E);print(2*_A+'-Retrieve organization');from ex_03_fhir import deleteResource as E;from fhir.resources.organization import Organization as J;from ex_05_fhir_create_custom import createOrRetrieveOrganizationOnServer as W;import uuid
	try:
		S=X+str(uuid.uuid4());D=J();D.name=S;G=W(D);A=G is not _B
		if A:
			P=W(D);A=G is not _B and G.id==P.id
			if G.id!=P.id:
				if G.id is not _B:E(G)
				if P.id is not _B:E(P)
			else:E(G)
	except:A=_C
	print(4*_A+(_D if A else _F)+_E)
def checkEx_6():
	print('Check 6 - Linking of custom FHIR objects');print(2*_A+'-Create custom encounter');
    from fhir.resources.reference import Reference as R;
    from ex_06_fhir_linking import createCustomEncounter as G;import random
	try:
		def X(pat_id,org_id):A=R(reference=_L+'/'+str(org_id));B=R(reference=_H+'/'+str(pat_id));C='finished';D=I(subject=B,serviceProvider=A,status=C);return D
		S=int(random.random()*1000000);T=int(random.random()*1000000);Y=X(S,T);Z=G(S,T);A=Y==Z
	except:A=_C
	print(4*_A+(_D if A else _F)+_E);print(2*_A+'-Lookup encounter');from ex_03_fhir import deleteResource as B,uploadResource as U;from fhir.resources.encounter import Encounter as I;
    from ex_06_fhir_linking import lookupCustomEncounterOnServer as V;from ex_05_fhir_create_custom import createCustomPatient as K,createCustomOrganization as L,createOrRetrievePatientOnServer as M,createOrRetrieveOrganizationOnServer as N;from ex_06_fhir_linking import createCustomEncounter as G;
    O=K();C=M(O);P=L();D=N(P);Q=_B
	try:
		F=G(C.id,D.id);H=V(F);A=H is _B
		if A:
			a=U(F);Q=I.parse_raw(a);H=V(F);A=H is not _B
			if H is not _B:B(H)
	except:
		A=_C
		if Q is not _B:B(Q)
	if D is not _B:B(D)
	if C is not _B:B(C)
	print(4*_A+(_D if A else _F)+_E);print(2*_A+'-Retrieve encounter');from ex_03_fhir import deleteResource as B;from fhir.resources.encounter import Encounter as I;
    from ex_06_fhir_linking import createOrRetrieveEncounterOnServer as W;from ex_05_fhir_create_custom import createCustomPatient as K,createCustomOrganization as L,createOrRetrievePatientOnServer as M,createOrRetrieveOrganizationOnServer as N;from ex_06_fhir_linking import createCustomEncounter as G;
    O=K();C=M(O);P=L();D=N(P)
	try:
		F=G(C.id,D.id);E=W(F);A=E is not _B
		if A:
			J=W(F);A=E is not _B and E.id==J.id
			if E.id!=J.id:
				if E.id is not _B:B(E)
				if J.id is not _B:B(J)
			else:B(E)
	except:A=_C
	if D is not _B:B(D)
	if C is not _B:B(C)
	print(4*_A+(_D if A else _F)+_E)
def checkEx_7():
	C='Encounter';print('Check 7 - Delete resources');print(2*_A+'-Delete all resources');from ex_03_fhir import loadResources as A;from ex_07_delete import deleteResources as D;import time
	try:
		E=A(_H,filter=_G);F=A(_L,filter=_G);G=A(C,filter=_G)
		if len(E)+len(F)+len(G)==0:print(6*_A+'Warning: No resources to delete. Test ignored.')
		D();time.sleep(5);H=A(_H,filter=_G);I=A(_L,filter=_G);J=A(C,filter=_G);B=len(H)+len(I)+len(J)==0
	except:B=_C
	print(4*_A+(_D if B else _F)+_E)
def main():
	if len(sys.argv)!=2 or sys.argv[1]not in[str(A)for A in range(8)]:print('No exercise number given.',file=sys.stderr);sys.exit(-1)
	A=int(sys.argv[1])
	if A==0:checkEx_0()
	if A==1:checkEx_1()
	if A==2:checkEx_2()
	import uuid;from Day7.ex_00_settings import test_updateRZKennung as B;B('test_' + str(uuid.uuid4()))
	if A==3:checkEx_3()
	if A==4:checkEx_4()
	if A==5:checkEx_5()
	if A==6:checkEx_6()
	if A==7:checkEx_7()
if __name__=='__main__':main()