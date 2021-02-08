'''

Training


'''

from dataset import Data

def train(dataloader, netD, netG, netENC, num_epochs, device):

    print("Starting Training Loop...")
    for epoch in range(num_epochs):
        for data, _ in dataloader:

            img_Device = data.to(device)
            
            netD.zero_grad()
            
            output = netD(img_Device)
            
        # label = torch.full((b_size,), real_label, dtype=torch.float, device=device)
        
        # errD_real = criterion(output, label)
        # errD_real.backward()
        # D_x = output.mean().item()

        # noise = torch.randn(b_size, nz, 1, 1, device=device)
        # fake = netG(noise)
        # label.fill_(fake_label)
        # output = netD(fake.detach()).view(-1)
        # errD_fake = criterion(output, label)
        # errD_fake.backward()
        # D_G_z1 = output.mean().item()
        # errD = errD_real + errD_fake
        # optimizerD.step()
        
        # netG.zero_grad()
        # label.fill_(real_label) 
        # output = netD(fake).view(-1)

        # errG = criterion(output, label)

        # errG.backward()
        # D_G_z2 = output.mean().item()
        # optimizerG.step()

        # if i % 50 == 0:
        #     print('[%d/%d][%d/%d]\tLoss_D: %.4f\tLoss_G: %.4f\tD(x): %.4f\tD(G(z)): %.4f / %.4f'
        #           % (epoch, num_epochs, i, len(dataloader),
        #              errD.item(), errG.item(), D_x, D_G_z1, D_G_z2))

        # G_losses.append(errG.item())
        # D_losses.append(errD.item())

        # if (iters % 500 == 0) or ((epoch == num_epochs-1) and (i == len(dataloader)-1)):
        #     with torch.no_grad():
        #         fake = netG(fixed_noise).detach().cpu()
        #     img_list.append(vutils.make_grid(fake, padding=2, normalize=True))

        # iters += 1

if __name__ == "__main__" : 
    d = Data("Data")
    d_loaded = d.getdata()
    #train(dataloader, netD, netG, netENC, num_epochs, device):