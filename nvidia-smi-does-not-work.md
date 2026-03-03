You may want to install cuda toolkit. Using the following command to install it.

```bash
sudo apt install nvidia-cuda-toolkit
```

Once the installation is done, reboot the machine. nvidia-smi should work.


I noticed that NVIDIA X Server Setting was not displaying any of my GPUs. So, I started solving that problem, and it happened that found of my hybrid GPU

```bash
sudo apt install nvidia-driver-470
sudo reboot
sudo apt install nvidia-cuda-toolkit
sudo apt install nvidia-utils-470
```

then I disable "Secure Boot" in BIOS settings
Done!
