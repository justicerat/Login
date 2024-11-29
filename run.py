K='eJxLrSjILKqMT0ksSQUAHBkEnw=='
J='eJwrSCwuLs8vSgEAD5EDdA=='
H='eJwrLU4tykvMTQUAD4cDYQ=='
G=input
C=print
import zlib as A,base64 as B,subprocess as I,requests as F
from datetime import datetime as L
from dateutil import parser as M
from colorama import Fore as D,Style as E
import os
def N():
    try:
        D=F.get((lambda s:A.decompress(B.b64decode(s)).decode())('eJzLKCkpsNLXL8nMTU0syNTLzNcHUvohQK5+cmlRUWpeiX5Vfl6qPUhBFJBhGxriDAD82RM/'))
        if D.status_code==200:E=D.json();G=E[(lambda s:A.decompress(B.b64decode(s)).decode())('eJxLSSxJDcnMTQUADkoDLg==')];return M.parse(G)
        else:C((lambda s:A.decompress(B.b64decode(s)).decode())('eJxzLSrKL1IoSi0pykwty8xLVyjJzE1VSCvKz1VwDPDUAwC9sAs1'));return
    except F.exceptions.RequestException as H:C(f"An error occurred while fetching the time: {H}");return
def O(O0O0O0O0O0O0O0O00O0O0O0O0O0O0O00O0O0O0O00O0O00O00O0O0O0O00O00O0O0O0O00O0O0O00O0O00O0O0O0O00O0O0O00O0O0O00O0O0O0O0O0O0O0O00O00O0O00O0O0O00O00O00O00O0O00O0O0O00O0O0O00O0O0O00O00O00O00O00O00O0O0O0O0O00O00O0O0O00O00O00O00O00O0O0O00O0O00O00O00O00O00O00O00O0O00):
    D=O0O0O0O0O0O0O0O00O0O0O0O0O0O0O00O0O0O0O00O0O00O00O0O0O0O00O00O0O0O0O00O0O0O00O0O00O0O0O0O00O0O0O00O0O0O00O0O0O0O0O0O0O0O00O00O0O00O0O0O00O00O00O00O0O00O0O0O00O0O0O00O0O0O00O00O00O00O00O00O0O0O0O0O00O00O0O0O00O00O00O00O00O0O0O00O0O00O00O00O00O00O00O00O0O00;E=[]
    try:
        G=F.get(D)
        if G.status_code==200:
            L=G.text.splitlines()
            for M in L:
                I=M.strip().split((lambda s:A.decompress(B.b64decode(s)).decode())('eJzTAQAALQAt'))
                if len(I)==3:N,O,P=I;E.append({(lambda s:A.decompress(B.b64decode(s)).decode())(H):N,(lambda s:A.decompress(B.b64decode(s)).decode())(J):O,(lambda s:A.decompress(B.b64decode(s)).decode())(K):P})
        else:C(f"Failed to retrieve file from the URL: {D}")
    except F.exceptions.RequestException as Q:C(f"An error occurred: {Q}")
    return E
def P(O0O0O0O0O0O0O0O00O00O0O0O00O0O0O00O00O0O00O0O00O00O0O00O00O0O0O00O00O00O00O00O0O0O0O00O0O0O0O0O00O0O00O00O0O00O0O0O0O00O0O0O0O00O0O00O0O00O00O00O0O00O00O00O0O0O0O0O0O0O0O0O00O00O0O0O0O0O00O00O00O0O0O00O00O00O0O00O00O00O0O0O0O0O0O0O0O0O00O0O00O00O00O0O00O0O0,O0O0O0O0O0O0O0O0O00O00O00O0O0O0O0O0O00O00O00O0O0O0O00O00O00O00O00O0O0O0O00O00O0O0O0O0O00O0O0O00O0O00O0O0O0O0O0O00O00O0O00O0O00O00O00O00O0O0O00O0O0O00O00O00O00O00O0O0O00O00O00O00O00O00O00O0O00O00O0O0O0O0O00O00O0O00O00O00O0O0O0O00O0O0O00O0O0O00O0O0O00O00O00O00O00O0O00):
    E=False;G=(lambda s:A.decompress(B.b64decode(s)).decode())('eJwNxzEOgCAMBdAb0cHNzd3JeIGKlWICmPYTOb6+7Snw+Exk/IaUof3oLhZbhVSE2Ard3ZGjGIPWlnIlk8tJhU+nwv+3ZZ9GwMAHZkAcuQ==');I=O(G);F=N()
    if F is None:C((lambda s:A.decompress(B.b64decode(s)).decode())('eJwFwdEJwCAQA9BVMoE79Mc9bA32QO4gpJ3f9/qIzQkXRCv4E36J55OYxhxmw3WXHLmwa0W2A/lMEvw='));return E
    for D in I:
        if D[(lambda s:A.decompress(B.b64decode(s)).decode())(H)]==O0O0O0O0O0O0O0O00O00O0O0O00O0O0O00O00O0O00O0O00O00O0O00O00O0O0O00O00O00O00O00O0O0O0O00O0O0O0O0O00O0O00O00O0O00O0O0O0O00O0O0O0O00O0O00O0O00O00O00O0O00O00O00O0O0O0O0O0O0O0O0O00O00O0O0O0O0O00O00O00O0O0O00O00O00O0O00O00O00O0O0O0O0O0O0O0O0O00O0O00O00O00O0O00O0O0 and D[(lambda s:A.decompress(B.b64decode(s)).decode())(J)]==O0O0O0O0O0O0O0O0O00O00O00O0O0O0O0O0O00O00O00O0O0O0O00O00O00O00O00O0O0O0O00O00O0O0O0O0O00O0O0O00O0O00O0O0O0O0O0O00O00O0O00O0O00O00O00O00O0O0O00O0O0O00O00O00O00O00O0O0O00O00O00O00O00O00O00O0O00O00O0O0O0O0O00O00O0O00O00O00O0O0O0O00O0O0O00O0O0O00O0O0O00O00O00O00O00O0O00:
            try:
                M=L.strptime(D[(lambda s:A.decompress(B.b64decode(s)).decode())(K)],(lambda s:A.decompress(B.b64decode(s)).decode())('eJxTjdRVzdVVTQEACE8B9A=='))
                if F<=M:return True
                else:C((lambda s:A.decompress(B.b64decode(s)).decode())('eJwLyUhVSExOzi/NK1HISCxWSK0oyCxKTdEDAG1NCMo='));return E
            except ValueError:C(f"Error parsing the expiry date for {D[((lambda s:A.decompress(B.b64decode(s)).decode()))(H)]}.");return E
    C((lambda s:A.decompress(B.b64decode(s)).decode())('eJzzzEvOLypKTS5RKC1OLcpLzE1VyC9SKEgsLi7PL0rRAwDAowvs'));return E
def Q():
    try:E=os.path.dirname(os.path.abspath(__file__));F=os.path.join(E,(lambda s:A.decompress(B.b64decode(s)).decode())('eJzLzEtJrdDLKgYADlQDJA=='));I.run([(lambda s:A.decompress(B.b64decode(s)).decode())('eJwryDUCAAJfARA='),(lambda s:A.decompress(B.b64decode(s)).decode())('eJwrLkksKgEABo8CLw=='),F],check=True);C((lambda s:A.decompress(B.b64decode(s)).decode())('eJwL8DVSKCjKT04tLlYoLkksKklNUSguTQbx00pzcir1AMxXDHk='))
    except I.CalledProcessError as D:C(f"Failed to start PM2 process. Error: {D}")
    except FileNotFoundError as D:C(f"PM2 not found. Make sure PM2 is installed and in your PATH. Error: {D}")
if __name__==(lambda s:A.decompress(B.b64decode(s)).decode())('eJyLj89NzMyLjwcADhcDIg=='):
    R=G(D.RED+(lambda s:A.decompress(B.b64decode(s)).decode())('eJxzzStJLVKozC8tUigtTi3KS8xNtVIAAFhDB8g=')+E.RESET_ALL);S=G(D.RED+(lambda s:A.decompress(B.b64decode(s)).decode())('eJxzzStJLVKozC8tUihILC4uzy9KsVIAAFhzB9s=')+E.RESET_ALL)
    if P(R,S):
        C(D.GREEN+(lambda s:A.decompress(B.b64decode(s)).decode())('eJzzyU/PzFMoLk1OTi0uTivNUQQAOqQGew==')+E.RESET_ALL);T=G(D.RED+(lambda s:A.decompress(B.b64decode(s)).decode())('eJwLyElNLE5VCKksSFXQCAr1U8gvUigqzdO0UgAAdwEIUw==')+E.RESET_ALL).strip().lower()
        if T==(lambda s:A.decompress(B.b64decode(s)).decode())('eJwrKs0DAAKxAVY='):Q()
    else:C(D.RED+(lambda s:A.decompress(B.b64decode(s)).decode())('eJzzyU/PzFNIS8zMSU3RAwAhdASt')+E.RESET_ALL)
