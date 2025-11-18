# 🔍 CSS Not Loading - Diagnostic Checklist

## Step 1: Check Browser Console
1. Open your site: https://travel-tribe-eajn.onrender.com/
2. Press F12 (or right-click → Inspect)
3. Go to "Console" tab
4. Look for errors like:
   - `Failed to load resource: the server responded with a status of 404`
   - `net::ERR_ABORTED 404 (Not Found)`

**What to look for:**
- If you see `/static/css/global.css` with 404 error → Static files not collected
- If you see `/static/css/global.css` with 500 error → Server error
- If no errors → CSS might be loading but with wrong content

## Step 2: Check Network Tab
1. In DevTools, go to "Network" tab
2. Refresh the page (Ctrl+R or Cmd+R)
3. Look for CSS files (filter by "CSS")
4. Check their status:
   - ✅ 200 = File loaded successfully
   - ❌ 404 = File not found
   - ❌ 500 = Server error

## Step 3: Try Direct CSS URL
Visit this URL directly in your browser:
```
https://travel-tribe-eajn.onrender.com/static/css/global.css
```

**Expected results:**
- ✅ Shows CSS code → Static files ARE working, issue is elsewhere
- ❌ 404 Not Found → Static files not collected properly
- ❌ 500 Server Error → Django/WhiteNoise configuration issue

## Step 4: Check Render Logs
1. Go to Render Dashboard
2. Click on your service
3. Click "Logs" tab
4. Look for:
   ```
   Collecting static files...
   X static files copied to '/opt/render/project/src/staticfiles'
   ```

**What to check:**
- If you see "0 static files copied" → Files not found
- If you see "X static files copied" where X > 0 → Files collected successfully

## Step 5: Tell Me What You See

Please tell me:
1. **Browser Console errors:** (copy-paste any red errors)
2. **Network tab status:** (200, 404, or 500 for CSS files?)
3. **Direct CSS URL result:** (Does it show CSS code or error?)
4. **Render logs:** (How many static files were copied?)

Based on your answers, I'll know exactly what to fix! 🔧

---

## Quick Fixes to Try

### If you see 404 errors:
The static files aren't being collected. Run locally:
```bash
python manage.py collectstatic --no-input
```
Then check if files appear in `staticfiles/` folder.

### If you see 500 errors:
There's a server configuration issue. Check Render logs for Python errors.

### If CSS loads but looks wrong:
Clear browser cache: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
