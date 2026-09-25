# sunrise SEO 記録

毎日のSEOチェック（毎朝8:52）の記録。新しい日付を上に追記する。

## 2026-09-25（3回目）
- 会社概要に表示されていた未記入の仮の文字（設立・許可番号）を非表示にした。検査・監視でも再発を検出するようにした。値をもらえたら表示する。
- 独自ドメインへの切り替え準備（DOMAIN を変えるだけで CNAME と監視先も切り替わる）。
- ops/owner-tasks.md にユーザー作業の手順と文面（Search Console、転送、Googleビジネスプロフィール、独自ドメイン、口コミ）を用意。

## 2026-09-25（2回目）
- 5分ごとの自動監視（GitHub Actions）を追加。ページ表示・リンク切れ・画像・タイトル/説明文/canonical/h1/構造化データ・noindex混入・表示速度・旧アドレス転送を確認し、異常時は Issue で通知。
- コラム一覧を /column → /column/ に変更（GitHub Pages で /column が開けない問題の対策）。

## 2026-09-25
- GitHub Pages（https://sasurainoebitiri-code.github.io/-sunrise/）へ移転。全14ページ・サイトマップ13URLを公開。
- 旧アドレス（sunrise-kaitai.pages.dev）からの301転送用 zip を redirect-cloudflare/ に用意（Cloudflareへのアップロードはユーザー作業）。
- Search Console: 新アドレスのプロパティ登録とサイトマップ送信はユーザー作業待ち。
