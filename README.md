
<p align="center">
  <a href="https://haniumer.com"><img src="https://img.shields.io/badge/Website-haniumer.com-000?style=for-the-badge&logo=safari&logoColor=white" alt="Website"/></a>
  <a href="https://git.h1n054ur.dev/h1n054ur"><img src="https://img.shields.io/badge/Forgejo-git.h1n054ur.dev-FB923C?style=for-the-badge&logo=forgejo&logoColor=white" alt="Forgejo"/></a>
  <a href="https://mailhide.io/e/w2H5EHRa"><img src="https://img.shields.io/badge/Email-Reveal_Address-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
  <img src="https://komarev.com/ghpvc/?username=h1n054ur&style=for-the-badge&color=blueviolet&label=Profile+Views" alt="Profile Views"/>
</p>

<p align="center">
  <a href="https://tinyurl.com/ecxpkcdc"><img src="https://tinyurl.com/5upvew82" alt="h1n0 Game" /></a>
</p>

```console
$ whoami
hani · sydney · building at borderless technology solutions
$ cat ~/.focus
edge-native products on cloudflare · self-hosted infra I can rebuild from git · security research done properly
```

<ul align="center">
  <a><b>Operating Principle</b>: Ship fast. Learn faster. Own the stack.</a>
</ul>

---

### ⚡ What I'm Focused On

- **Cloudflare-native products.** Whole apps on one Worker: D1, R2, KV, Durable Objects, Queues, Email Workers. Most of my public work and the product line at Borderless Technology Solutions (status pages, file sharing, forums, CMS, AI support chat) ships this way.
- **Self-hosted infrastructure.** A Proxmox homelab of LXC containers, k3s, Forgejo with HA failover and its own CI runners, all behind Tailscale and Cloudflare Tunnel, all rebuildable from git.
- **Ethical security research.** Teaching labs and documented analysis, authorized testing only.
- **Tools for my own workflow.** MCP servers, Claude Code skills, Discord and Telegram bots, a Linux desktop (CachyOS + Hyprland) set up as code.

> 🔐 Security projects here are strictly for **educational and authorized testing only**.  
No malware, no unauthorized deployment.

```mermaid
flowchart LR
    dev["laptop + desktop<br/>CachyOS · Hyprland · kitty"] -->|git push| forgejo["Forgejo HA<br/>git.h1n054ur.dev"]
    forgejo -->|mirror| github["GitHub"]
    forgejo -->|Forgejo Actions| runners["self-hosted runners"]
    runners -->|wrangler deploy| edge["Cloudflare<br/>Workers · D1 · R2 · DO · Queues"]
    runners -->|compose deploy| lab["Proxmox homelab<br/>LXC · k3s · Docker"]
    lab --- tunnel["Cloudflare Tunnel<br/>+ Tailscale"]
    tunnel --- edge
```

---

### 🛠️ Things I've Built

<table>
<tr>
<td valign="top" width="33%">

#### `// edge`
- [**Uptellis**](https://github.com/bts-io/uptellis) status page + monitor, Workers or Docker
- [**0bin-cloudflare**](https://github.com/h1n054ur/0bin-cloudflare) encrypted pastebin on one Worker
- [**elm-chat**](https://github.com/h1n054ur/elm-chat) E2EE rooms on Durable Objects
- [**hookforms-cloud**](https://github.com/h1n054ur/hookforms-cloud) webhook inbox, multi-channel alerts
- [**PingFlare**](https://github.com/h1n054ur/PingFlare) Statuspage alternative
- [**vinext-starter**](https://github.com/h1n054ur/vinext-starter) Next.js API on Vite, on Workers

</td>
<td valign="top" width="33%">

#### `// infra`
- [**vps-git**](https://github.com/h1n054ur/vps-git) Forgejo HA, streaming replication, failover, Ansible
- [**hookforms**](https://github.com/h1n054ur/hookforms) self-hosted webhook inbox
- [**docker-browser**](https://github.com/h1n054ur/docker-browser) remote browser via neko + cloudflared
- [**h1n054ur-terminal**](https://github.com/h1n054ur/h1n054ur-terminal) welcome banner + starship prompt
- [**telegram-cloudflare-relay**](https://github.com/h1n054ur/telegram-cloudflare-relay) Telegram to anywhere

</td>
<td valign="top" width="33%">

#### `// security + ai`
- [**botnet-research-archive**](https://github.com/h1n054ur/botnet-research-archive) historical botnets mapped to MITRE ATT&CK
- [**ghost-lab**](https://github.com/h1n054ur/ghost-lab) browser-native C2 research lab
- [**keystroke-monitor**](https://github.com/h1n054ur/keystroke-monitor) authorized-testing lab on Workers
- [**playwright-mcp-cloudflare**](https://github.com/h1n054ur/playwright-mcp-cloudflare) browser MCP on Workers
- [**chat-first-ui-builder**](https://github.com/h1n054ur/chat-first-ui-builder) UI by conversation, Hono JSX + Claude

</td>
</tr>
</table>

---

### 📡 Live

<table>
<tr>
<td valign="top" width="50%">

#### `// latest releases`
<!--LIVE:RELEASES:START-->
- [**uptellis**](https://github.com/bts-io/uptellis) [`v0.8.4`](https://github.com/bts-io/uptellis/releases/tag/v0.8.4) <sub>2 days ago</sub>
- [**0bin-cloudflare**](https://github.com/h1n054ur/0bin-cloudflare) [`v0.2.0`](https://github.com/h1n054ur/0bin-cloudflare/releases/tag/v0.2.0) <sub>3 days ago</sub>
- [**vps-git**](https://github.com/h1n054ur/vps-git) [`v2.0.0`](https://github.com/h1n054ur/vps-git/releases/tag/v2.0.0) <sub>9 days ago</sub>
<!--LIVE:RELEASES:END-->

</td>
<td valign="top" width="50%">

#### `// recently pushed`
<!--LIVE:PUSHED:START-->
- [**uptellis**](https://github.com/bts-io/uptellis) <sub>2 days ago</sub>
- [**0bin-cloudflare**](https://github.com/h1n054ur/0bin-cloudflare) <sub>2 days ago</sub>
- [**h1n054ur-terminal**](https://github.com/h1n054ur/h1n054ur-terminal) <sub>2 days ago</sub>
- [**vps-git**](https://github.com/h1n054ur/vps-git) <sub>2 days ago</sub>
- [**elm-chat**](https://github.com/h1n054ur/elm-chat) <sub>3 days ago</sub>
<!--LIVE:PUSHED:END-->

</td>
</tr>
</table>

<p align="center">
<!--LIVE:STATS:START-->
<sub>Last 12 months: <b>572</b> contributions · <b>488</b> commits · <b>32</b> PRs · <b>22</b> issues · <b>45</b> public repos. Refreshed 2026-10-06.</sub>
<!--LIVE:STATS:END-->
</p>

<p align="center">
  <img width="49%" src="./profile/stats.svg" alt="GitHub Stats"/>
  <img width="49%" src="./profile/top-langs.svg" alt="Top Languages"/>
</p>

<p align="center">
  <img width="60%" src="./profile/streak.svg" alt="GitHub Streak"/>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: light)" srcset="./profile/snake-light.svg"/>
    <img width="100%" src="./profile/snake-dark.svg" alt="Contribution snake"/>
  </picture>
</p>

---

### 🧰 Stack

<table>
<tr>
<td width="18%"><code>// languages</code></td>
<td><img height="40" src="./assets/stack/languages.svg" alt="TypeScript, JavaScript, Python, Bash, C"/></td>
</tr>
<tr>
<td><code>// edge apps</code></td>
<td>
  <img height="40" src="./assets/stack/edge.svg" alt="Cloudflare, Workers, React, Vite, Tailwind, Bun, Node.js, SQLite/D1, Vitest, Astro"/><br/>
  <img src="https://img.shields.io/badge/Hono-E36002?style=flat-square&logo=hono&logoColor=white"/>
  <img src="https://img.shields.io/badge/TanStack_Start-000?style=flat-square&logo=tanstack&logoColor=white"/>
  <img src="https://img.shields.io/badge/Drizzle-C5F74F?style=flat-square&logo=drizzle&logoColor=black"/>
  <img src="https://img.shields.io/badge/Zod-3E67B1?style=flat-square&logo=zod&logoColor=white"/>
  <img src="https://img.shields.io/badge/Better_Auth-000?style=flat-square&logo=betterauth&logoColor=white"/>
</td>
</tr>
<tr>
<td><code>// infra</code></td>
<td>
  <img height="40" src="./assets/stack/infra.svg" alt="Linux, Arch, Debian, Docker, Kubernetes, Ansible, PostgreSQL, Grafana, GitHub Actions, Git"/><br/>
  <img src="https://img.shields.io/badge/Proxmox-E57000?style=flat-square&logo=proxmox&logoColor=white"/>
  <img src="https://img.shields.io/badge/Forgejo-FB923C?style=flat-square&logo=forgejo&logoColor=white"/>
  <img src="https://img.shields.io/badge/Tailscale-242424?style=flat-square&logo=tailscale&logoColor=white"/>
  <img src="https://img.shields.io/badge/Cloudflare_Tunnel-F38020?style=flat-square&logo=cloudflare&logoColor=white"/>
  <img src="https://img.shields.io/badge/Hyprland-58E1FF?style=flat-square&logo=hyprland&logoColor=black"/>
</td>
</tr>
</table>

---

<p align="center">
  <img src="https://img.shields.io/badge/Built_with-Obsession-ff6b35?style=flat-square"/>
  <img src="https://img.shields.io/badge/Powered_by-Coffee_&_Chaos-6F4E37?style=flat-square"/>
  <img src="https://img.shields.io/badge/Status-Always_Building-58a6ff?style=flat-square"/>
</p>

<p align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=58A6FF&center=true&vCenter=true&random=false&width=600&lines=%24+whoami;Edge-native+products+on+Cloudflare;Self-hosted+infra%2C+rebuildable+from+git;Breaking+things+to+understand+them;Now+is+better+than+never." alt="Typing SVG" />
  </a>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12&height=100&section=footer" width="100%"/>
</p>
