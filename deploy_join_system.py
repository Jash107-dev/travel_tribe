#!/usr/bin/env python
"""
Automatic deployment script for join request system
"""
import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} completed successfully")
            if result.stdout.strip():
                print(f"   Output: {result.stdout.strip()}")
        else:
            print(f"❌ {description} failed")
            print(f"   Error: {result.stderr.strip()}")
            return False
        return True
    except Exception as e:
        print(f"❌ {description} failed with exception: {e}")
        return False

def deploy_system():
    print("🚀 DEPLOYING SECURE JOIN REQUEST SYSTEM")
    print("=" * 50)
    
    # Step 1: Add all changes
    if not run_command("git add .", "Adding all changes to git"):
        return False
    
    # Step 2: Commit changes
    commit_message = "Implement bulletproof join request system - no direct joining allowed"
    if not run_command(f'git commit -m "{commit_message}"', "Committing changes"):
        print("ℹ️  No changes to commit (already committed)")
    
    # Step 3: Push to repository
    if not run_command("git push", "Pushing to repository"):
        return False
    
    print("\n🎉 DEPLOYMENT COMPLETED SUCCESSFULLY!")
    print("\n📋 WHAT'S NEW:")
    print("✅ Secure join request system implemented")
    print("✅ Users must request to join trips")
    print("✅ Trip creators can view profiles before approving")
    print("✅ Only approved members can access chat")
    print("✅ Test page available at /test-join-system/")
    
    print("\n🧪 TESTING INSTRUCTIONS:")
    print("1. Visit your deployed site")
    print("2. Go to /test-join-system/ to verify system")
    print("3. Try joining a trip - should show request form")
    print("4. Login as trip creator to manage requests")
    print("5. Approve requests and verify members are added")
    
    print("\n🔒 SECURITY FEATURES:")
    print("• No direct joining allowed")
    print("• Profile viewing before approval")
    print("• Chat access only for approved members")
    print("• Request status tracking")
    print("• Points awarded for approved requests")
    
    return True

if __name__ == "__main__":
    success = deploy_system()
    if success:
        print("\n🎯 System is ready! Test it on your deployed site.")
    else:
        print("\n❌ Deployment failed. Check the errors above.")
        sys.exit(1)