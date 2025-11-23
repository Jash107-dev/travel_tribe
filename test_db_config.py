#!/usr/bin/env python3
"""
Test database configuration for Render deployment
"""
import dj_database_url

def test_db_config():
    """Test that our database configuration is valid"""
    
    # Test with a sample PostgreSQL URL (like Render provides)
    test_url = "postgresql://user:pass@host:5432/dbname"
    
    try:
        # This should work without errors
        config = dj_database_url.config(
            default=test_url,
            conn_max_age=600,
            conn_health_checks=True,
        )
        
        print("✅ Database configuration is valid!")
        print(f"Engine: {config['ENGINE']}")
        print(f"Name: {config['NAME']}")
        print(f"Host: {config['HOST']}")
        print(f"Port: {config['PORT']}")
        print(f"Conn Max Age: {config['CONN_MAX_AGE']}")
        return True
        
    except Exception as e:
        print(f"❌ Database configuration error: {e}")
        return False

if __name__ == '__main__':
    test_db_config()