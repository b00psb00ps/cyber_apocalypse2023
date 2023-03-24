# Cyber Apocalypse 2023

## Drobots

> Pandora's latest mission as part of her reconnaissance training is to infiltrate the Drobots firm that was suspected of engaging in illegal activities.
> Can you help pandora with this task?
> 
> [`source_code`](web_drobots.zip)

## Solution

Browsing through the source code we can see a comment referring to the lack of sanitization for logging in, suggesting SQLi is our vector of attack;

![source-code-discovery](unsanitized_login.png)

So we'll try a basic SQLi login bypass;

![sqli-payload](sqli_payload.png)

And just like that we retrieved the flag;

![flag](flag.png)

Flag `HTB{p4r4m3t3r1z4t10n_1s_1mp0rt4nt!!!}`
