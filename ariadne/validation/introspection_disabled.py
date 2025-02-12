from graphql3 import GraphQLError
from graphql3.language import FieldNode
from graphql3.validation import ValidationRule

from ..contrib.tracing.utils import is_introspection_key


class IntrospectionDisabledRule(ValidationRule):
    def enter_field(self, node: FieldNode, *_args):
        field_name = node.name.value
        if not is_introspection_key(field_name):
            return

        self.report_error(
            GraphQLError(
                f"Cannot query '{field_name}': introspection is disabled.",
                node,
            )
        )
