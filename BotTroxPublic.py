# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess

cl = LINETCR.LINE() #Bot Utama
cl.login(token="Eqek1vC7KLnK4jsWnYb0.fGIUiExEjuE1/OChSHYIia.I+U46H+FbaNeyUFj6q8tYpNBQ7cKfoHlCQ972Cv50fg=")
cl.loginResult()

print "BotTrox Public Bot"
reload(sys)
sys.setdefaultencoding('utf-8')

#album = None
#image_path = 'tmp/tmp.jpg'
mulai = time.time()

helpMessage ="""BOTTROX PUBLIC BOT

👉 .dan say <text>
👉 .youtube <content>
👉 .instagram <username]
👉 .creator
👉 /apakah <kata - kata>
👉 love | Contoh = M love K
👉 .quotes
👉 .cek <TanggalLahir>
👉 .wiki-id [ Wikipedia Indonesia ]
👉 .wiki-en [ Wikipedia English ]
👉 Gcreator [ Group Creator ]
👉 /say-id  - /say-en 
👉 @bye - Mengeluarkan Bot
👉 tagall
=========================
             ADMIN ONLY
=========================
👉 Admadd @ [ Admin Add ]
👉 Admrm @ [ Remove Admin]
👉 .alist [Admin List ]
👉 .cbc [ Contact BroadCast ]
👉 .gbc [ Group BroadCast ]
👉 .spm [ .spm 5 Test ]
👉 Gurl [ Buka QR > Link QR ]
👉 Cancel [ Rombongan ]
👉 reject [ Undangan Grup ]
👉 Mid @
👉 Tempeleng @
👉 Play @


sᴜᴘᴘᴏʀᴛ ʙʏ
BOTTROX PUBLIC"""

KAC=[cl]
mid = cl.getProfile().mid

Bots=[mid]
admin=["u1608ae21e5de2547b5fa8707b21ca220"]
creator=["u1608ae21e5de2547b5fa8707b21ca220"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":20},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Thanks sudah mengadd DanBot\n\nuntuk menginvite DanBot, anggota grup harus melebihi 20.\n\nCreator: line://ti/p/~danrfq",
    "lang":"JP",
    "comment":"Auto Like by DanBot",
    "commentOn":True,
    "clock":True,
    "welcomemsg":True,
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendImage(self, to_, path):
      M = Message(to=to_,contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M_id = self.Talk.client.sendMessage(0,M).id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True
      
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik.' % (hours, mins, secs)

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except Exception as e:
         raise e
 
def post_content(self, urls, data=None, files=None):
        return self._session.post(urls, headers=self._headers, data=data, files=files)

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n9§9" + Name
                wait2['ROM'][op.param1][op.param2] = "9§9" + Name
        else:
            pass
    except:
        pass
        
def sendAudio(self, to_, path):
        M = Message(to=to_, text=None, contentType = 3)
        M_id = self.Talk.client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)            
        }       

        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        print r
        if r.status_code != 201:
            raise Exception('Upload audio failure.')    


def sendAudioWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download audio failure.')
      try:
         self.sendAudio(to_, path)
      except Exception as e:
            raise e
            
def sendVoice(self, to_, path):
        M = Message(to=to_, text=None, contentType = 3)
        M.contentPreview = None
        M_id = self._client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'voice_message',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload voice failure.')
        return True            
                 

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        if op.type == 17:
           if op.param2 in Bots:
              return
           ginfo = cl.getGroup(op.param1)
           random.choice(KAC).sendText(op.param1, "Selamat Datang Di Grup  " + str(ginfo.name))
           random.choice(KAC).sendText(op.param1, "Pembuat Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName)
#           random.choice(KAC).sendText(op.param1,"Budayakan Baca Note !!! yah Kak 😊\nSemoga Betah Yak Boleh Invite Temen Juga Kok 😘")
           print "MEMBER HAS JOIN THE GROUP"
        if op.type == 15:
           if op.param2 in Bots:
              return
           random.choice(KAC).sendText(op.param1, "dih leave.")
           print "MEMBER HAS LEFT THE GROUP"

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                        	cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                            cl.sendText(op.param1,"Terimakasih telah mengundang DanBot\nUntuk melihat fitur2 DanBot, silahkan ketik /help")
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        cl.sendText(op.param1,"Terimakasih telah mengundang DanBot\nUntuk melihat fitur2 DanBot, silahkan ketik /help")
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
                    
        if op.type == 17:
	   if wait["welcomemsg"] == True:
              if op.param2 not in Bots:
                 ginfo = cl.getGroup(op.param1)
                 cinfo = cl.getContact(op.param2)
                 cl.sendText(op.param1,str(cinfo.displayName)+"\nSelamat Datang Di Grup "+str(ginfo.name))
                 cl.sendImageWithURL(op.param1,"http://dl.profile.line-cdn.net/"+str(cinfo.pictureStatus))
                 c = Message(to=op.param1, from_=None, text=None, contentType=13)
                 c.contentMetadata={'mid':op.param2}
                 cl.sendMessage(c)

        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)

        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
                cl.comment(url[25:58],url[66:],wait["comment"])

            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URL0‰96¥9¡¯\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","/help","Help"]:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,helpMessage)
					else:
						cl.sendText(msg.to,helpt)
            elif ("Gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("Gn ","")
						cl.updateGroup(X)
					else:
						cl.sendText(msg.to,"It can't be used besides the group.")

            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)


            elif "Ginfo" in msg.text:
                    group = cl.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak ditemukan"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventJoinByTicket == True:
                        gQr = "Tertutup"
                        gTicket = "Tidak ada"
                    else:
                        gQr = "Terbuka"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    ret_ = "╔════════Grup Info═════════"
                    ret_ += "\n╠Nama Grup : {}".format(group.name)
                    ret_ += "\n╠ID Grup : {}".format(group.id)
                    ret_ += "\n╠Pembuat Grup : {}".format(gCreator)
                    ret_ += "\n╠Jumlah Member : {}".format(str(len(group.members)))
                    ret_ += "\n╠Jumlah Pending : {}".format(gPending)
                    ret_ += "\n╠Grup QR : {}".format(gQr)
                    ret_ += "\n╠Grup URL : {}".format(gTicket)
                    ret_ += "\n╚════════Grup Info═════════"
                    cl.sendText(msg.to, str(ret_))
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
            elif "gid" == msg.text:
				if msg.from_ in admin:
					cl.sendText(msg.to,msg.to)
            elif "Mid" == msg.text:
					cl.sendText(msg.to,msg.from_)

            elif msg.text in ["Wkwk"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "100",
										"STKPKGID": "1",
										"STKVER": "100" }
					cl.sendMessage(msg)
					cl.sendMessage(msg)
            elif msg.text in ["Hehehe"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "10",
										"STKPKGID": "1",
										"STKVER": "100" }
					cl.sendMessage(msg)
					cl.sendMessage(msg)
            elif msg.text in ["Galon"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "9",
										"STKPKGID": "1",
										"STKVER": "100" }
					cl.sendMessage(msg)
					cl.sendMessage(msg)
            elif msg.text in ["You"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "7",
										"STKPKGID": "1",
										"STKVER": "100" }
					cl.sendMessage(msg)
					cl.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "6",
										"STKPKGID": "1",
										"STKVER": "100" }
					cl.sendMessage(msg)
					cl.sendMessage(msg)
            elif msg.text in ["Please"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "4",
										"STKPKGID": "1",
										"STKVER": "100" }
					cl.sendMessage(msg)
					cl.sendMessage(msg)
            elif msg.text in ["Haaa"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "3",
										"STKPKGID": "1",
										"STKVER": "100" }
					cl.sendMessage(msg)
					cl.sendMessage(msg)
            elif msg.text in ["Lol"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "110",
										"STKPKGID": "1",
										"STKVER": "100" }
					cl.sendMessage(msg)
					cl.sendMessage(msg)
            elif msg.text in ["Hmmm"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "101",
										"STKPKGID": "1",
										"STKVER": "100" }
					cl.sendMessage(msg)
            elif msg.text in ["Wc"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "247",
										"STKPKGID": "3",
										"STKVER": "100" }
					cl.sendMessage(msg)
					cl.sendMessage(msg)
            elif msg.text in ["TL:"]:
				if msg.from_ in admin:
					tl_text = msg.text.replace("TL: ","")
					cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Cn "]:
				if msg.from_ in admin:
					string = msg.text.replace("Cn ","")
					if len(string.decode('utf-8')) <= 9820:
						profile = cl.getProfile()
						profile.displayName = string
						cl.updateProfile(profile)
						cl.sendText(msg.to,"name " + string + " done")

            elif msg.text in ["reject"]:
				if msg.from_ in admin:
					gid = cl.getGroupIdsInvited()
					for i in gid:
						cl.rejectGroupInvitation(i)
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"All invitations have been refused")
					else:
						cl.sendText(msg.to,"Ã¦â€¹â„1¤7™Ã§Â»ÂÃ¤Âºâ„1¤7 Ã¥â„1¤7¦Â¨Ã©Æ’Â¨Ã§Å¡â„1¤7žÃ©â„1¤7šâ‚¬Ã¨Â¯Â·Ã£â‚¬â„1¤7„1¤7")

            elif msg.text in ["Up"]:
				if msg.from_ in admin:
					if wait["clock"] == True:
						now2 = datetime.now()
						nowT = datetime.strftime(now2,"(%H:%M)")
						profile = cl.getProfile()
						profile.displayName = wait["cName"] + nowT
						cl.updateProfile(profile)
						cl.sendText(msg.to,"Updated")
					else:
						cl.sendText(msg.to,"Please turn on the name clock")
					
            elif msg.text.lower() == 'restart':
              if msg.from_ in admin:
                    print "[Command]RESTART BOT"
                    try:
                        cl.sendText(msg.to,"Sukses Merestart Bot")
                        restart_program()
                    except:
                        cl.sendText(msg.to,"Please wait")
                        restart_program()
                        pass


            elif msg.text == "Check":
                    cl.sendText(msg.to, "Check sider Eror"),
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "Absen":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "People who readed %s\nthat's it\n\nPeople who have ignored reads\n%sIt is abnormal 7¬8\n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\n¡¸set¡¹you can send 7¬8 read point will be created 7¬8")
#-----------------------------------------------
            elif msg.text in ["Tagall","!cipok"]:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                cb = ""
                cb2 = ""
                strt = int(0)
                akh = int(0)
                for md in nama:
                    akh = akh + int(5)
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                    strt = strt + int(6)
                    akh = akh + 1
                    cb2 += "@nrik\n"
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                try:
                    cl.sendMessage(msg)
                except Exception as error:
                    print error
#-----------------------------------------------
            elif msg.text in ["out","@bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.sendText(msg.to,":(")
                        cl.leaveGroup(msg.to)
                    except:  
											pass
#-----------------------------------------------
            elif "Steal gpict" in msg.text:
					group = cl.getGroup(msg.to)
					path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
					cl.sendImageWithURL(msg.to, path)
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"Link QR Grup : \nline://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Glist" in msg.text:
                if msg.from_ in admin:
                        gid = cl.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            h += "☢ %s  \n" % (cl.getGroup(i).name + " 👥 ▶ [ " + str(len (cl.getGroup(i).members))+" ]")
                        cl.sendText(msg.to, "     ☢ [ ♡List Grup♡ ] ☜\n"+ h +"Total Group ▶" +"[ "+str(len(gid))+" ]")
            elif ".all" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						print "ok"
						_name = msg.text.replace(".all","")
						gs = cl.getGroup(msg.to)
						cl.sendText(msg.to,"Perintah DiLaksanakan Maaf Kan Saya :v Ã´")
						cl.sendText(msg.to,"Group DiBersihkan.")
						targets = []
						for g in gs.members:
							if _name in g.displayName:
								targets.append(g.mid)
						if targets == []:
							cl.sendText(msg.to,"Not found.")
							cl.sendText(msg.to,"Not found.")
						else:
							for target in targets:
								try:
									klist=[cl]
									kicker=random.choice(klist)
									kicker.kickoutFromGroup(msg.to,[target])
									print (msg.to,[g.mid])
								except:
									cl.sendText(msg.to,"Group cleanse")
									cl.sendText(msg.to,"Group cleanse")

#-----------------------------------------------
            elif "Tempeleng " in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      cl.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
#-------------------------------------------
#------------------------------------------
#-------------------[ResponBOT]---------------------------
            elif msg.text in [".test"]:
				if msg.from_ in admin:
					cl.sendText(msg.to,"Hadir Boss Qu!!")
					cl.sendText(msg.to,"DanBot Selalu Hadir Demi Kakak Tersayang")
#-----------------------------------------------
            elif ".dan say " in msg.text:
					bctxt = msg.text.replace(".dan say ","")
					cl.sendText(msg.to,(bctxt))
            elif msg.text in [".creator"]:
					msg.contentType = 13
					msg.contentMetadata = {'mid': 'u1608ae21e5de2547b5fa8707b21ca220'}
					cl.sendMessage(msg)
            elif msg.text in ["cancel","Cancel"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                        cl.sendText(msg.to,"Sukses Mengancel Undangan")
                    else:
                        cl.sendText(msg.to,"No one is inviting")
                else:
                    cl.sendText(msg.to,"Can not be used outside the group")
#-------------Fungsi Creator Finish-----------------#
            elif "Spam: " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam: ")+str(txt[1])+" "+str(jmlh + " ","")
                tulisan = jmlh * (teks+"\n")
                 #@reno.a.w
                if txt[1] == "on":
                    if jmlh <= 1000:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Kelebihan batas:v")
                elif txt[1] == "off":
                    if jmlh <= 1000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Kelebihan batas :v")
#----------------------------------------------------
            elif "Ds" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Ds ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                else:
                    cl.sendText(msg.to,"Done")
#-----------------------------------------------
            elif "Dn" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Dn ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
#-----------------------------------------------
            elif ".apakah " in msg.text:
                tanya = msg.text.replace("Apakah ","")
                jawab = ("Ya","Tidak","Bisa Jadi","Mungkin")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
#-----------------------------------------------
            elif "love " in msg.text:
                tanya = msg.text.replace("love ","")
                jawab = ("10%","20%","30%","40%","50%","60%","70%","80%","90%","100%\nKeterangan Moga - Moga Langgeng Ya Kak","0%\nKeterangan Ngak Cinta Sama Sekali :v")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
#-----------------------------------------------
            elif msg.text in ["Gcreator:inv"]:
	           if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       cl.findAndAddContactsByMid(gCreator)
                       cl.inviteIntoGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass
#----------------------------------------------               
#-------------------------------------------------------------
            elif ".gbc " in msg.text:
               if msg.from_ in admin:
                 bctxt = msg.text.replace(".gbc ", "")
                 n = cl.getGroupIdsJoined()
                 for manusia in n:
                    cl.sendText(manusia, (bctxt))

            elif ".cbc " in msg.text:
               if msg.from_ in admin:
                 bctxt = msg.text.replace(".cbc ", "")
                 t = cl.getAllContactIds()
                 for manusia in t:
                    cl.sendText(manusia, (bctxt))
#-----------------------------------------
#----------------------------------------------------------
            elif "Meikarta: " in msg.text:
                if msg.from_ in creator:
                    gid = msg.text.replace("Meikarta: ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            cl.findAndAddContactsByMid(msg.from_)
                            cl.inviteIntoGroup(gid,[msg.from_])
                        except:
                            cl.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
            elif "Play " in msg.text:
               if msg.from_ in admin:
                remove0 = msg.text.replace("Play ","")
                remove1 = remove0.lstrip()
                remove2 = remove1.replace("@","")
                remove3 = remove2.rstrip()
                _name = remove3
                groups = cl.getGroup(msg.to)
                targets = []
                for s in groups.members:
                    if _name == s.displayName:
                        targets.append(s.mid)
                if targets == []:
                    pass
                else:
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                            cl.findAndAddContactsByMid(target)
                            cl.inviteIntoGroup(msg.to,[target])
                            cl.cancelGroupInvitation(msg.to,[target])
                            cl.inviteIntoGroup(msg.to,[target])
                            cl.sendText(msg.to,"You have been slain!")
                        except:
                            cl.sendText(msg.to,"Error, your account limit.")
                            break
 #---------------------------------- SONG ------------------------------------
            elif ".lirik" in msg.text.lower():
                songname = msg.text.replace("/lirik","")
                params = {"songname":songname}
                r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                data = r.text
                data = json.loads(data)
                for song in data:
                    cl.sendText(msg.to,song[5])
                    print "[Command] Lirik"

            elif ".music" in msg.text.lower():
                songname = msg.text.replace(".music","")
                params = {"songname":songname}
                r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                data = r.text
                data = json.loads(data)
                for song in data:
                    cl.sendText(msg.to,"Judul : " + song[0] + "\nDurasi : " + song[1])
                    cl.sendText(msg.to,song[4])
                    print "[Command] Lagu"
#----------------------------------------------------------------------------
#--------------------------------- INSTAGRAM --------------------------------
#--------------------------------- INSTAGRAM --------------------------------
            elif '.instagram' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace(".instagram ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO USER========\n"
                    details = "\n========INSTAGRAM INFO USER========"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
#----------------------------------------------------------------------------
            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                dan = "Waktu Keaktifan DanBot\n「"+waktu(eltime)+"」"
                cl.sendText(msg.to,dan)
#-------------------------------------
                                    
            elif "Dcopy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Dcopy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Tidak Ada...")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Berhasil Menyalin Profil")
                                except Exception as e:
                                    print e
                                    
            elif msg.text in ["Dbackup"]:
                try:
                    cl.updateDisplayPicture(mybackup.pictureStatus)
                    cl.updateProfile(mybackup)
                    cl.sendText(msg.to, "Backup Done!!")
                except Exception as e:
                    cl.sendText(msg.to, str (e))
#-------------------------------------
#------------------------------------------------------------------
            elif "Steal dp @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Steal dp @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
 #---------------------------------- SONG ------------------------------------
#--------------------------------- YOUTUBE ----------------------------------
            elif ".youtube" in msg.text:
                query = msg.text.replace(".youtube ","")
                with requests.session() as s:
                    s.headers['user-agent'] = 'Mozilla/5.0'
                    url = 'http://www.youtube.com/results'
                    params = {'search_query': query}
                    r = s.get(url, params=params)
                    soup = BeautifulSoup(r.content, 'html5lib')
                    hasil = ""
                    for a in soup.select('.yt-lockup-title > a[title]'):
                        if '&list=' not in a['href']:
                            hasil += ''.join((a['title'],'\nhttp://www.youtube.com' + a['href'],'\n\n'))
                    cl.sendText(msg.to,hasil)
                    print '[Command] Youtube Search'
#----------------------------------------------------------------------------
#-----------------------------------------------------
            elif ".cek" in msg.text:
                tanggal = msg.text.replace(".cek ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                cl.sendText(msg.to,"Tanggal Lahir: "+lahir+"\n\nUsia: "+usia+"\n\nUltah: "+ultah+"\n\nZodiak: "+zodiak)
#-----------------------------------------------------
#--------------------------------- TRANSLATE --------------------------------
            elif "/translate-en" in msg.text:
                txt = msg.text.replace("/translate-en","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'en')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate EN'
                except:
                    cl.sendText(msg.to,'Error Karena Anda Jelek')

            elif "/translate-id" in msg.text:
                txt = msg.text.replace("/translate-id","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'id')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate ID'
                except:
                    cl.sendText(msg.to,'Error Karena Anda Jelek')
#---------------------------------------
#-------------Fungsi Spam Start---------------------#
            elif msg.text in [".up","P"]:
            	if msg.from_ in admin:
                  cl.sendText(msg.to,"Spam!")
                  cl.sendText(msg.to,"Spam!􏿿")
                  cl.sendText(msg.to,"Nsibdhdkfndifnhfnfbfjfjfn")
                  cl.sendText(msg.to,"Nsvdhdjbdjdjfbdjjfbfd")
                  cl.sendText(msg.to,"Bsjdjbdkfnfnfjifjfbf")
                  cl.sendText(msg.to,"legalporno.com")
                  cl.sendText(msg.to,"javhihi.com")
                  cl.sendText(msg.to,"Skhdjdbdbjfjf")
                  cl.sendText(msg.to,"Jjshdhdhjdjfhfhfhjfjf")
                  cl.sendText(msg.to,"Jjdjdbfbfjjfnfkfjfnjfbbfbfb!􏿿")
                  cl.sendText(msg.to,"Ndjbfbfbfifjfbjfbf")
                  cl.sendText(msg.to,"janvhihi.com!􏿿")
                  cl.sendText(msg.to,"Legalpprno.com")
                  cl.sendText(msg.to,"Spam")
                  cl.sendText(msg.to,"HdhdhdjjfbjjHHhjbh")
                  cl.sendText(msg.to,"PNsjdbjdkfbfjfjfbbd")
                  cl.sendText(msg.to,"mangasusus.blogspot.com!􏿿")
                  cl.sendText(msg.to,"Spam")
                  cl.sendText(msg.to,"Anggotanya Suka Makan Micin!􏿿")
                  cl.sendText(msg.to,"Suka Nonton Bokep Lagi!􏿿")
                  cl.sendText(msg.to,"Hadeh Dasar Nak Jaman Now!􏿿")
                  cl.sendText(msg.to,"nekopoi.host")
                  cl.sendText(msg.to,"legalporno.com")
                  cl.sendText(msg.to,"javhihi.com")
                  cl.sendText(msg.to,"Nsnhdbdbd")
                  cl.sendText(msg.to,"Ndjdjfbfnjf")
                  cl.sendText(msg.to,"Spam Hampir Selesai")
                  cl.sendText(msg.to,"W Udahan Spam Nya")
                  cl.sendText(msg.to,"Capek Ahhh Nulisnya!􏿿")
                  cl.sendText(msg.to,"Done!􏿿")
            elif msg.text in ["Welcomemsg on"]:
               if msg.from_ in admin:
                if wait["welcomemsg"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Turned To ON\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Turned To ON\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["welcomemsg"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Turned To ON\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already ON")
            elif msg.text in ["Welcomemsg off"]:
              if msg.from_ in admin:
                if wait["welcomemsg"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["welcomemsg"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
#-------------Fungsi Broadcast Start------------#
#--------------Fungsi Broadcast Finish-----------#                           
            elif msg.text in ["Gcreator"]:
              if msg.toType == 2:
                    msg.contentType = 13
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                        msg.contentMetadata = {'mid': gCreator}
                        gCreator1 = ginfo.creator.displayName
                        
                    except:
                        gCreator = "Error"
                    cl.sendText(msg.to, "Group Creator : " + gCreator1)
                    cl.sendMessage(msg)
#-----------------------------------------------
            elif "Admadd @" in msg.text:
                if msg.from_ in creator:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Admadd @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                cl.sendText(msg.to,"Admin Telah Ditambahkan")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command Di Tolak Jangan Sedih")
                    cl.sendText(msg.to,"Sudah Menjadi Admin Maka Tidak Bisa Menjadi Admin Lagi")

            elif "Admrm @" in msg.text:
                if msg.from_ in creator:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Admrm @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                cl.sendText(msg.to,"Admin Telah Dihapus")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command DiTolak")
                    cl.sendText(msg.to,"Admin Tidak Bisa Menggunakan")

            elif msg.text in ["Adminlist",".alist"]:
              if msg.from_ in creator:
                if admin == []:
                    cl.sendText(msg.to,"The adminlist is empty")
                else:
                    cl.sendText(msg.to,"Sabar Dikit Mamang.....")
                    mc = ""
                    for mi_d in admin:
                        mc += "☢ " +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"
#-----------------------------------------------
            if msg.text in ["Raisa"]:
                    try:
                        cl.sendImageWithURL(msg.to, "https://cdn.brilio.net/news/2017/05/10/125611/750xauto-selalu-tampil-cantik-memesona-ini-harga-10-sepatu-raisa-andriana-170510q.jpg")
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                        
            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'u1608ae21e5de2547b5fa8707b21ca220'}
                cl.sendMessage(msg)
                profile = cl.getProfile(receiver)
                xname = profile.displayName
                xlen = str(len(xname)+1)
                msg.contentType = 0
                msg.text = "@"+xname+" :)"
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(mid)+'}]}','EMTVER':'4'}
                cl.sendMessage(msg)
#-----------------------------------------------
            elif "kapan" in msg.text:
                tanya = msg.text.replace("kapan","")
                jawab = ("Besok","Tahun Depan","Minggu Depan","Satu Abad Lagi")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
#-----------------------------------------------
            elif ".waktu" in msg.text:
	    	       wait2['setTime'][msg.to] = datetime.today().strftime('TANGGAL : %Y-%m-%d \nHARI : %A \nJAM : %H:%M:%S')
	               cl.sendText(msg.to, "         Waktu/Tanggal\n\n" + (wait2['setTime'][msg.to]))
	               cl.sendText(msg.to, "Mungkin Tidak Sesuai Atau Sesuai Dengan Tanggal/Waktu Sekrang Dikarenakan Ini Robot Bukan Manusia :v")
#-----------------------------------------------
#-----------------------------------------------
            elif ".quotes" in msg.text:
                tanya = msg.text.replace(".quotes","")
                jawab = ("Manusia hendaknya mulai dari detik ini juga mengusahakan dengan tidak pernah jemu untuk memahami hakekat Kebajikan/kebenaran, Kekayaan, Kesenangan, dan Kebebasan. Manusia adalah Sang Raja bagi dirinya sendiri, ia adalah pemimpin dari tubuhnya, ia adalah penguasa dari pikirannya; maka dari itu, berusahalah untuk memahami hakekat penjelmaan ini","Janganlah pernah bersedih hati dilahirkan menjadi manusia, meskipun pada kelahiran yang dianggap paling hina; karena sesungguhnya amat sulit untuk bisa menjelma menjadi manusia. Berbahagialah menjadi manusia","Mereka yang telah melakukan kebajikan pun kebenaran, namun masih terikat dalam proses lahir dan mati, mereka ini belumlah memperoleh inti sari dari kebebasan","Kebajikan dan kebenaran itu laksana perahu yang dapat mengantarkan manusia untuk pergi ke surga","Mustahil ada persahabatan tanpa kesabaran hati, yang ada pastilah kemurkaan, marah dan dendam, maka dari itu pupuklah terus kesabaran di dalam hati masing-masing")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
#----------------------------------------------------------------                  
            elif "/apakah" in msg.text:
                  tanya = msg.text.replace("/apakah","")
                  jawab = ("ya","tidak","Bisa jadi","mungkin")
                  jawaban = random.choice(jawab)
#-------------------------------------------------
#-----------------------------------------------
            elif msg.text in ["pap","Pap"]:
                        cl.sendImageWithURL(msg.to, "https://i.pinimg.com/736x/d1/93/25/d19325b71789e33bedb054468c1fd134--girls-generation-tiffany-girls-generation.jpg")
            elif msg.text in ["kam"]:
				if msg.from_ in admin:
					cl.sendText(msg.to,"Selamat datang di Group")
					cl.sendText(msg.to,"Jangan nakal ok!")
#-----------------------------------------------
#--------------------------------- DUGEM ------------------------------------
            elif ".kedapkedip " in msg.text.lower():
                txt = msg.text.replace(".kedapkedip ", "")
                cl.kedapkedip(msg.to,txt)
                print "[Command] Kedapkedip"
#--------------------------------------------------------------------------
            elif "Hay @" in msg.text:
                _name = msg.text.replace("Hay @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(g.mid,"Your Account Has Been Spammed !")
                       cl.sendText(g.mid,"Your Account Has Been Spammed !")  
                       cl.sendText(g.mid,"Your Account Has Been Spammed !")  
                       cl.sendText(g.mid,"Your Account Has Been Spammed !")
                       cl.sendText(g.mid,"Your Account Has Been Spammed !")  
                       cl.sendText(g.mid,"Your Account Has Been Spammed !")  
                       cl.sendText(g.mid,"Your Account Has Been Spammed !")
                       cl.sendText(msg.to, "Done")
                       print " Spammed !"
#---------------------------- SPAM CHAT -------------------------------------
            elif ".spm" in msg.text:
                if msg.from_ in admin:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[1])
                    teks = msg.text.replace(".spm " + str(jmlh) + " ","")
                    if jmlh <= 9999:
                        for x in range(jmlh):
                            cl.sendText(msg.to,teks)
#-------------------------------------------------
            elif '.wiki-id' in msg.text.lower():
                  try:
                      wiki = msg.text.lower().replace(".wiki-id ","")
                      wikipedia.set_lang("id")
                      wiki = WikiApi({'locale':'id'})
                      results = wicl.find("search")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Text Nya Kepanjagan Klik Link Ini Saja\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))                             
 #-------------------------------------------------
            elif '.wiki-en' in msg.text.lower():
                  try:
                      wiki = msg.text.lower().replace(".wiki-en ","")
                      wikipedia.set_lang("en")
                      wiki = WikiApi({'locale':'en'})
                      results = wicl.find("search")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
#-----------------------------------------------
            elif msg.text in [".res",".respon"]:
				if msg.from_ in admin:
					cl.sendText(msg.to,"SATRIA Bot Hadir ")
            elif msg.text in ["Dinv"]:
              if msg.from_ in admin:
                wait["ricoinvite"] = True
                random.choice(KAC).sendText(msg.to,"Mana kontaknya?")
#-------------------------------------------------
            elif "/say-id" in msg.text:
                say = msg.text.replace("/say-id","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
#------------------------------------------------
#-------------------------------------------------
            elif "/say-en" in msg.text:
                say = msg.text.replace("/say-en","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
#------------------------------------------------
            elif "Mid @" in msg.text:
                  _name = msg.text.replace("Mid @","")
                  _nametarget = _name.rstrip(' ')
                  gs = cl.getGroup(msg.to)
                  for g in gs.members:
                      if _nametarget == g.displayName:
                          cl.sendText(msg.to, g.mid)
                      else:
                          pass
#----------------------------------------------------------------------------
#---------------------------------------
            elif ".say" in msg.text.lower():
                    query = msg.text.replace(".say","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'id', 'speed': '1', 'query': query}
                        r    = s.get(url, params=params)
                        mp3  = r.url
                        cl.sendAudio(msg.to, mp3)
#--------------------------------------------------------
            elif msg.text in ["Sp","Speed",".sp"]:
				if msg.from_ in admin:
					start = time.time()
					cl.sendText(msg.to, "Lagi Proses...")
					elapsed_time = time.time() - start
					cl.sendText(msg.to, "%s Detik" % (elapsed_time))
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)  
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
