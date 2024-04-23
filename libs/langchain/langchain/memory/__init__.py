"""**Memory** maintains Chain state, incorporating context from past runs.

**Class hierarchy for Memory:**

.. code-block::

    BaseMemory --> BaseChatMemory --> <name>Memory  # Examples: ZepMemory, MotorheadMemory

**Main helpers:**

.. code-block::

    BaseChatMessageHistory

**Chat Message History** stores the chat message history in different stores.

**Class hierarchy for ChatMessageHistory:**

.. code-block::

    BaseChatMessageHistory --> <name>ChatMessageHistory  # Example: ZepChatMessageHistory

**Main helpers:**

.. code-block::

    AIMessage, BaseMessage, HumanMessage
"""  # noqa: E501
from langchain_community.chat_message_histories import (
    AstraDBChatMessageHistory,
    CassandraChatMessageHistory,
    ChatMessageHistory,
    CosmosDBChatMessageHistory,
    DynamoDBChatMessageHistory,
    ElasticsearchChatMessageHistory,
    FileChatMessageHistory,
    MomentoChatMessageHistory,
    MongoDBChatMessageHistory,
    PostgresChatMessageHistory,
    RedisChatMessageHistory,
    SingleStoreDBChatMessageHistory,
    SQLChatMessageHistory,
    StreamlitChatMessageHistory,
    UpstashRedisChatMessageHistory,
    XataChatMessageHistory,
    ZepChatMessageHistory,
)
from langchain_community.memory import (
    ConversationKGMemory,
    MotorheadMemory,
    RedisEntityStore,
    SQLiteEntityStore,
    UpstashRedisEntityStore,
    ZepMemory,
)
from langchain_core.legacy.memory import (
    CombinedMemory,
    ConversationBufferMemory,
    ConversationBufferWindowMemory,
    ConversationEntityMemory,
    ConversationStringBufferMemory,
    ConversationSummaryBufferMemory,
    ConversationSummaryMemory,
    ConversationTokenBufferMemory,
    InMemoryEntityStore,
    ReadOnlySharedMemory,
    SimpleMemory,
    VectorStoreRetrieverMemory,
)

__all__ = [
    "AstraDBChatMessageHistory",
    "CassandraChatMessageHistory",
    "ChatMessageHistory",
    "CombinedMemory",
    "ConversationBufferMemory",
    "ConversationBufferWindowMemory",
    "ConversationEntityMemory",
    "ConversationKGMemory",
    "ConversationStringBufferMemory",
    "ConversationSummaryBufferMemory",
    "ConversationSummaryMemory",
    "ConversationTokenBufferMemory",
    "CosmosDBChatMessageHistory",
    "DynamoDBChatMessageHistory",
    "ElasticsearchChatMessageHistory",
    "FileChatMessageHistory",
    "InMemoryEntityStore",
    "MomentoChatMessageHistory",
    "MongoDBChatMessageHistory",
    "MotorheadMemory",
    "PostgresChatMessageHistory",
    "ReadOnlySharedMemory",
    "RedisChatMessageHistory",
    "RedisEntityStore",
    "SingleStoreDBChatMessageHistory",
    "SQLChatMessageHistory",
    "SQLiteEntityStore",
    "SimpleMemory",
    "StreamlitChatMessageHistory",
    "VectorStoreRetrieverMemory",
    "XataChatMessageHistory",
    "ZepChatMessageHistory",
    "ZepMemory",
    "UpstashRedisEntityStore",
    "UpstashRedisChatMessageHistory",
]
