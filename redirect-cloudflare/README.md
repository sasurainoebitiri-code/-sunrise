# 旧アドレスからの転送（Cloudflare Pages 用）

`sunrise-redirect.zip` を Cloudflare の **sunrise-kaitai** プロジェクトにデプロイすると、
`https://sunrise-kaitai.pages.dev/…` へのアクセスがすべて
`https://sunrise-kaitai.github.io/…` に 301（恒久的な移転）で転送されます。
（例: `/building` → `https://sunrise-kaitai.github.io/building`。ページの場所はそのまま引き継がれます）

手順: Cloudflare ダッシュボード → Workers & Pages → sunrise-kaitai → 「新しいデプロイを作成」→ zip を展開した中身（または zip）をドラッグ → デプロイ。

中身は `files/` フォルダと同じです。
