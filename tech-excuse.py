#!/usr/bin/env python
import random

array1 = ["Temporary","Intermittant","Partial","Redundant","Total","Multiplexed","Inherent","Duplicated",
					"Dual-homed","Synchronous","Bidirectional","Serial","Asynchronous","Multiple","Replicated",
					"Non-replicated","Unregistered","Non-specific","Generic","Migrated","Localised","Resignalled",
					"Dereferenced","Nullified","Aborted","Serious","Minor","Major","Extraneous","Illegal",
					"Insufficient","Viral","Unsupported","Outmoded","Legacy","Permanent","Invalid","Deprecated",
					"Virtual","Unreportable","Undetermined","Undiagnosable","Unfiltered","Static","Dynamic",
					"Delayed","Immediate","Nonfatal","Fatal","Non-valid","Unvalidated","Non-static",
					"Unreplicatable","Non-serious","Hot","Cold","Internal","External","Hidden"]

array2 = ["temporary","intermittant","partial","redundant","total","multiplexed","inherent","duplicated",
					"dual-homed","synchronous","bidirectional","serial","asynchronous","multiple","replicated",
					"non-replicated","unregistered","non-specific","generic","migrated","localised","resignalled",
					"dereferenced","nullified","aborted","serious","minor","major","extraneous","illegal",
					"insufficient","viral","unsupported","outmoded","legacy","permanent","invalid","deprecated",
					"virtual","unreportable","undetermined","undiagnosable","unfiltered","static","dynamic",
					"delayed","immediate","nonfatal","fatal","non-valid","unvalidated","non-static",
					"unreplicatable","non-serious","hot","cold","internal","external","hidden"]

array3 = ["array","systems","hardware","software","firmware","backplane","logic-subsystem",
					"integrity","subsystem","memory","comms","integrity","checksum","protocol","parity","bus",
					"timing","synchronisation","topology","transmission","reception","stack","framing","code","backup",
					"programming","peripheral","environmental","loading","operation","parameter","syntax","context",
					"initialisation","execution","resource","encryption","decryption","file","precondition","raid",
					"authentication","paging","swapfile","service","gateway","request","proxy","media","CRC",
					"registry","configuration","codec","metadata","streaming","retrieval","installation","library",
					"handler"]

array4 = ["interruption","destabilisation","interlude","destruction","abnormality","desynchronisation",
					"dereferencing", "overflow","variance","underflow","nmi","inconsistency","interrupt","corruption",
					"reclock","rejection","invalidation","intrusion","halt","exhaustion","infection","incompatibility",
					"timeout","obliteration","expiry","glitch","unavailability","bug","condition","crash","dump","crashdump",
					"problem","lockout","failure","anomaly","seizure","override","incongruity","stackdump","clash",
					"disturbance","error","feature","problem","warning","signal","flag","irregularity","abnormality"]


print(random.choice(array1) + ", " + random.choice(array2) + " " + random.choice(array3) + " " + random.choice(array4))
