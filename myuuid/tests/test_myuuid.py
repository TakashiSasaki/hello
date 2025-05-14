#filename: tests/test_myuuid.py
# 
import uuid
import pytest
from myuuid import get_new_uuidv5, MY_NAMESPACE_UUID

def test_get_new_uuidv5_returns_uuid_object():
    """get_new_uuidv5 が UUID オブジェクトを返すことを確認"""
    name = "test_name"
    result = get_new_uuidv5(name)
    assert isinstance(result, uuid.UUID)

def test_get_new_uuidv5_returns_version5():
    """get_new_uuidv5 が UUID バージョン5を返すことを確認"""
    name = "test_name"
    result = get_new_uuidv5(name)
    assert result.version == 5

def test_get_new_uuidv5_is_deterministic():
    """同じ入力に対して常に同じUUIDを返すことを確認 (決定性)"""
    name = "deterministic_test"
    result1 = get_new_uuidv5(name)
    result2 = get_new_uuidv5(name)
    assert result1 == result2

def test_get_new_uuidv5_returns_different_uuids_for_different_names():
    """異なる入力に対して異なるUUIDを返すことを確認"""
    name1 = "name_one"
    name2 = "name_two" # name1とは異なる名前
    result1 = get_new_uuidv5(name1)
    result2 = get_new_uuidv5(name2)
    assert result1 != result2

def test_get_new_uuidv5_uses_correct_namespace():
    """UUIDが想定された名前空間UUIDを使用して生成されていることを確認"""
    # uuid5(namespace, name) は、namespaceとnameからハッシュ値を計算し、
    # そのハッシュ値からUUIDを生成します。
    # 同じnamespaceとnameであれば、uuid.uuid5は常に同じ値を返します。
    # ここでは、myuuidモジュールが公開しているMY_NAMESPACE_UUIDが
    # 内部的に使用されていることを、決定性テストによって間接的に確認済みですが、
    # より直接的にテストしたい場合は、既知の入力に対する期待される出力UUIDを
    # ハードコードして比較することも可能です。
    # 例: 特定の名前空間と名前に対する既知のUUID5を計算しておき比較
    known_namespace = uuid.UUID('c8ee7542-57d0-4fb3-880a-739391e7c131')
    test_name = "known_test_name"
    expected_uuid = uuid.uuid5(known_namespace, test_name)

    actual_uuid = get_new_uuidv5(test_name)

    assert actual_uuid == expected_uuid
    # さらに、get_new_uuidv5の内部で使われているMY_NAMESPACE_UUIDが
    # 想定通りの値であることもここで確認しておくとより安全
    assert MY_NAMESPACE_UUID == known_namespace


def test_get_new_uuidv5_handles_various_string_inputs():
    """様々な文字列入力で正しく動作することを確認"""
    assert isinstance(get_new_uuidv5(""), uuid.UUID) # 空文字列
    assert isinstance(get_new_uuidv5("日本語テスト"), uuid.UUID) # 日本語
    assert isinstance(get_new_uuidv5("!@#$%^&*()"), uuid.UUID) # 特殊文字
    # 同じ文字列ならUUIDは同じ
    assert get_new_uuidv5("テスト") == get_new_uuidv5("テスト")
    # 大文字小文字は区別される (uuid5の仕様)
    assert get_new_uuidv5("TestName") != get_new_uuidv5("testname")

# 必要に応じて、名前空間UUID自体のテストも追加可能
# def test_my_namespace_uuid_is_constant():
#     """定義されている名前空間UUIDが期待する値であることを確認"""
#     assert str(MY_NAMESPACE_UUID) == 'c8ee7542-57d0-4fb3-880a-739391e7c131'