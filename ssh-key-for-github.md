# Setting Up an SSH Key for `git push`

This guide explains how to configure SSH so that work authored by:

```
fake-sophron500ac@gmail.com
```

can be pushed to the repository:

```
https://github.com/FemtoEmacs/cell2sequence_guide/
```

---

## Overview

To push code securely to GitHub without using passwords, you must:

1. Create an SSH key
2. Add the public key to your GitHub account
3. Configure your repository to use SSH instead of HTTPS
4. Push your changes

---

## Step 1 — Create an SSH Key

Open a terminal and run:

```bash
ssh-keygen -t ed25519 -C "fake-sophron500ac@gmail.com"
```

When prompted:

```
Enter file in which to save the key (/home/your-user/.ssh/id_ed25519):
```

Press **Enter** to accept the default location.

You may set a passphrase or press Enter to skip.

This creates:

```
~/.ssh/id_ed25519       (private key — keep secret)
~/.ssh/id_ed25519.pub   (public key — upload to GitHub)
```

---

## Step 2 — Add the SSH Key to GitHub

Display your public key:

```bash
cat ~/.ssh/id_ed25519.pub
```

Copy the entire output.

Then:

1. Go to https://github.com/settings/keys
2. Click **New SSH Key**
3. Give it a title (e.g., "Laptop")
4. Paste the public key
5. Click **Add SSH Key**

---

## Step 3 — Test SSH Authentication

Run:

```bash
ssh -T git@github.com
```

Expected output:

```
Hi FemtoEmacs! You've successfully authenticated, but GitHub does not provide shell access.
```

This confirms SSH is correctly configured.

---

## Step 4 — Configure the Repository to Use SSH

Your repository URL is currently:

```
https://github.com/FemtoEmacs/cell2sequence_guide/
```

Git push will fail over HTTPS unless you use a token.  
Instead, switch the remote to SSH.

Inside the repository directory, run:

```bash
git remote set-url origin git@github.com:FemtoEmacs/cell2sequence_guide.git
```

Verify:

```bash
git remote -v
```

You should see:

```
git@github.com:FemtoEmacs/cell2sequence_guide.git
```

---

## Step 5 — Push Your Work

Now push:

```bash
git add .
git commit -m "React to cell2sentence."
git push
```

Your changes should upload successfully without requiring a password.

---

## Optional — If SSH Agent Is Needed

If you encounter authentication issues, start the SSH agent:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

---

## Done

You can now securely push commits authored by:

```
fake-sophron500ac@gmail.com
```

to:

```
https://github.com/FemtoEmacs/cell2sequence_guide/
```

using SSH authentication.
````
