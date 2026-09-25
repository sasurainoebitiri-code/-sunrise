# sunrise SEO 記録

毎日のSEOチェック（毎朝8:52）の記録。新しい日付を上に追記する。

## 2026-09-25（7回目）
- Search Console: トップ・building・interior・restore・asbestos のインデックス登録をリクエスト（ユーザーが Chrome の Claude で実施）。
- Googleビジネスプロフィール: 「株式会社sunrise」を登録（サービス地域 5県）。ステータスは「処理しています」＝Google の確認待ち。確認が終わると検索・マップに表示される。
- Google 広告は使わない（ユーザー方針：まずは無料のみ）。

## 2026-09-25（6回目）
- 検索結果の見た目の改善: トップに WebSite 構造化データ（サイト名「株式会社sunrise」）を追加、会社情報にロゴ・写真を追加。反映は Google の再クロール後（数日〜数週間）。

## 2026-09-25（5回目）
- https://sunrise-kaitai.github.io/ へ引っ越し・公開完了（監視も成功）。
- Search Console: 新アドレス（URLプレフィックス https://sunrise-kaitai.github.io/）の所有者確認完了（HTMLファイル方式。確認用ファイル google8acb34de16487f3d.html は build.py の GSC_FILES。消さないこと）。sitemap.xml 送信済み（ユーザー操作）。

## 2026-09-25（4回目）
- ユーザーの希望で、無料アドレス https://sunrise-kaitai.github.io/ へ移ることに決定。サイト・転送zip・手順書を新アドレス向けに更新（作業ブランチで準備。引っ越し完了後に公開）。

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
