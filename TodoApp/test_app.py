"""
Test script for Todo App
Simple tests to verify basic functionality
"""

import os
import sys
import tempfile
from datetime import datetime

# Add the current directory to path to import our modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from file_manager import TodoFileManager, validate_todo_file
    print("✅ Successfully imported file_manager module")
except ImportError as e:
    print(f"❌ Failed to import file_manager: {e}")
    sys.exit(1)

def test_file_manager():
    """Test the TodoFileManager functionality"""
    print("\n🧪 Testing TodoFileManager...")
    
    # Create a temporary file for testing
    temp_file = "test_todos.txt"
    backup_file = "test_todos_backup.txt"
    
    try:
        # Initialize file manager
        fm = TodoFileManager(temp_file, backup_file)
        
        # Test 1: Add todos
        print("Test 1: Adding todos...")
        assert fm.add_todo("Complete project", "High") == True
        assert fm.add_todo("Review code", "Medium") == True
        assert fm.add_todo("Update docs", "Low") == True
        print("✅ Successfully added todos")
        
        # Test 2: Read todos
        print("Test 2: Reading todos...")
        todos = fm.read_todos()
        assert len(todos) == 3
        assert todos[0]['task'] == "Complete project"
        assert todos[0]['priority'] == "High"
        assert todos[0]['status'] == "Pending"
        print("✅ Successfully read todos")
        
        # Test 3: Update todo status
        print("Test 3: Updating todo status...")
        assert fm.update_todo_status(0, "Completed") == True
        todos = fm.read_todos()
        assert todos[0]['status'] == "Completed"
        print("✅ Successfully updated todo status")
        
        # Test 4: Update todo task
        print("Test 4: Updating todo task...")
        assert fm.update_todo_task(1, "Review and test code") == True
        todos = fm.read_todos()
        assert todos[1]['task'] == "Review and test code"
        print("✅ Successfully updated todo task")
        
        # Test 5: Delete todo
        print("Test 5: Deleting todo...")
        assert fm.delete_todo(2) == True
        todos = fm.read_todos()
        assert len(todos) == 2
        print("✅ Successfully deleted todo")
        
        # Test 6: Statistics
        print("Test 6: Getting statistics...")
        stats = fm.get_statistics()
        assert stats['total'] == 2
        assert stats['completed'] == 1
        assert stats['pending'] == 1
        print("✅ Statistics working correctly")
        
        # Test 7: Search
        print("Test 7: Searching todos...")
        results = fm.search_todos("review")
        assert len(results) == 1
        assert "Review" in results[0]['task']
        print("✅ Search functionality working")
        
        # Test 8: Clear completed
        print("Test 8: Clearing completed todos...")
        assert fm.clear_completed() == True
        todos = fm.read_todos()
        assert len(todos) == 1
        assert todos[0]['status'] == "Pending"
        print("✅ Successfully cleared completed todos")
        
        # Test 9: Backup and restore
        print("Test 9: Backup and restore...")
        assert fm.create_backup() == True
        assert os.path.exists(backup_file)
        
        # Add a new todo and then restore
        fm.add_todo("Test todo", "Medium")
        todos_before_restore = fm.read_todos()
        assert len(todos_before_restore) == 2
        
        assert fm.restore_backup() == True
        todos_after_restore = fm.read_todos()
        assert len(todos_after_restore) == 1
        print("✅ Backup and restore working correctly")
        
        # Test 10: Export
        print("Test 10: Export functionality...")
        export_file = "test_export.txt"
        assert fm.export_todos(export_file, "txt") == True
        assert os.path.exists(export_file)
        
        # Check export content
        with open(export_file, 'r', encoding='utf-8') as f:
            content = f.read()
            assert "TODO LIST EXPORT" in content
            assert "PENDING TASKS" in content
        print("✅ Export functionality working")
        
        print("\n🎉 All TodoFileManager tests passed!")
        
    except AssertionError as e:
        print(f"❌ Test failed: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False
    finally:
        # Clean up test files
        for file in [temp_file, backup_file, export_file]:
            if os.path.exists(file):
                os.remove(file)
                
    return True

def test_file_validation():
    """Test the file validation functionality"""
    print("\n🧪 Testing file validation...")
    
    try:
        # Test valid file
        valid_content = """2024-10-24 10:30:15|High|Pending|Test task 1
2024-10-24 11:45:22|Medium|Completed|Test task 2"""
        
        test_file = "test_validation.txt"
        with open(test_file, 'w', encoding='utf-8') as f:
            f.write(valid_content)
        
        assert validate_todo_file(test_file) == True
        print("✅ Valid file validation passed")
        
        # Test invalid file
        invalid_content = """Invalid line format
2024-10-24 10:30:15|High|Pending"""  # Missing task field
        
        with open(test_file, 'w', encoding='utf-8') as f:
            f.write(invalid_content)
        
        assert validate_todo_file(test_file) == False
        print("✅ Invalid file validation passed")
        
        # Clean up
        if os.path.exists(test_file):
            os.remove(test_file)
            
        print("🎉 File validation tests passed!")
        return True
        
    except Exception as e:
        print(f"❌ File validation test failed: {e}")
        return False

def test_config_import():
    """Test configuration import"""
    print("\n🧪 Testing configuration import...")
    
    try:
        from config import APP_CONFIG
        
        # Check required config keys
        required_keys = ['window_title', 'window_size', 'theme', 'priorities']
        for key in required_keys:
            assert key in APP_CONFIG, f"Missing config key: {key}"
        
        # Check theme config
        theme_keys = ['bg_color', 'primary_color', 'font_family']
        for key in theme_keys:
            assert key in APP_CONFIG['theme'], f"Missing theme key: {key}"
            
        print("✅ Configuration import successful")
        print(f"   - Window title: {APP_CONFIG['window_title']}")
        print(f"   - Window size: {APP_CONFIG['window_size']}")
        print(f"   - Priorities: {APP_CONFIG['priorities']}")
        
        return True
        
    except Exception as e:
        print(f"❌ Configuration test failed: {e}")
        return False

def test_gui_import():
    """Test GUI module import (without starting GUI)"""
    print("\n🧪 Testing GUI module import...")
    
    try:
        # Test basic version import
        import todo_app
        print("✅ Basic todo_app module imported successfully")
        
        # Test enhanced version import  
        import enhanced_todo_app
        print("✅ Enhanced todo_app module imported successfully")
        
        # Test if we can create the class (without initializing GUI)
        assert hasattr(enhanced_todo_app, 'EnhancedTodoApp')
        print("✅ EnhancedTodoApp class found")
        
        return True
        
    except Exception as e:
        print(f"❌ GUI import test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 Starting Todo App Tests...")
    print("=" * 50)
    
    tests = [
        ("Configuration Import", test_config_import),
        ("File Manager", test_file_manager),
        ("File Validation", test_file_validation),
        ("GUI Module Import", test_gui_import),
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n📋 Running {test_name} test...")
        result = test_func()
        results.append((test_name, result))
    
    # Summary
    print("\n" + "=" * 50)
    print("🏁 Test Results Summary:")
    print("=" * 50)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The Todo App is ready to use.")
        print("\nTo start the app, run:")
        print("   python run_app.py")
        print("   or")
        print("   python enhanced_todo_app.py")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)