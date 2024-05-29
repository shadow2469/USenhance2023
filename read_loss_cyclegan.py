import os 
import matplotlib.pyplot as plt 



# 打开文件并使用readlines读取所有行
with open('/home/user9/USenhance2023/checkpoints/cyclegan_ultrasound_800/loss_log.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 打印文件内容
D_A = []
G_A = []
cycle_A = []
idt_A = []
D_B = []
G_B = []
cycle_B = []
idt_B = []
epoch = []
all_loss = []
last_epoch = 1
for line in lines[1:]:
    cur_epoch = int(line.split("epoch: ")[1].split(",")[0])
    if cur_epoch != last_epoch:
        
        last_epoch = cur_epoch
        tmp = 0
        D_A.append(float(da))
        G_A.append(float(ga))
        cycle_A.append(float(ca))
        idt_A.append(float(idta))
        D_B.append(float(db))
        G_B.append(float(gb))
        cycle_B.append(float(cb))
        idt_B.append(float(idtb))
        
        tmp += float(da)
        tmp += float(ga)
        tmp += float(ca)
        tmp += float(idta)
        tmp += float(db)
        tmp += float(gb)
        tmp += float(cb)
        tmp += float(idtb)
        all_loss.append(tmp)
    da = line.split("D_A: ")[1].split(" ")[0]
    ga = line.split("G_A: ")[1].split(" ")[0]
    ca = line.split("cycle_A: ")[1].split(" ")[0]
    idta = line.split("idt_A: ")[1].split(" ")[0]
    db = line.split("D_B: ")[1].split(" ")[0]
    gb = line.split("G_B: ")[1].split(" ")[0]
    cb = line.split("cycle_B: ")[1].split(" ")[0]
    idtb = line.split("idt_B: ")[1].split(" ")[0]
        


plt.plot(D_A)

plt.xlabel("epoches")
plt.ylabel("D_A loss")
plt.savefig("/home/user9/USenhance2023/cyclegan_loss/da.jpg")
plt.cla()
plt.plot(G_A)
plt.xlabel("epoches")
plt.ylabel("G_A loss")
plt.savefig("/home/user9/USenhance2023/cyclegan_loss/ga.jpg")
plt.cla()
plt.plot(cycle_A)
plt.xlabel("epoches")
plt.ylabel("Cycle_A loss")
plt.savefig("/home/user9/USenhance2023/cyclegan_loss/ca.jpg")
plt.cla()
plt.plot(idt_A)
plt.xlabel("epoches")
plt.ylabel("idt_A loss")
plt.savefig("/home/user9/USenhance2023/cyclegan_loss/idta.jpg")
plt.cla()
plt.plot(D_B)
plt.xlabel("epoches")
plt.ylabel("D_B loss")
plt.savefig("/home/user9/USenhance2023/cyclegan_loss/db.jpg")
plt.cla()
plt.plot(G_B)
plt.xlabel("epoches")
plt.ylabel("G_B loss")
plt.savefig("/home/user9/USenhance2023/cyclegan_loss/gb.jpg")
plt.cla()
plt.plot(cycle_B)
plt.xlabel("epoches")
plt.ylabel("Cycle_B loss")
plt.savefig("/home/user9/USenhance2023/cyclegan_loss/cb.jpg")
plt.cla()
plt.plot(idt_B)
plt.xlabel("epoches")
plt.ylabel("idt_B loss")
plt.savefig("/home/user9/USenhance2023/cyclegan_loss/idtb.jpg")
plt.cla()
plt.plot(all_loss)
plt.xlabel("epoches")
plt.ylabel("all loss")
plt.savefig("/home/user9/USenhance2023/cyclegan_loss/all.jpg")
plt.cla()
        