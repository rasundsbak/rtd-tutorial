exports.createPages = async function ({ actions, graphql }) {
    const { data } = await graphql(` /* some graphQL query */ `);
    data.allMarkdownRemark.edges.forEach((edge) => {
        const alternativeHtml = generateAlternativeHtml(edge.node.html);
        actions.createPage({
            component: require.resolve(`./src/templates/PostTemplate.jsx`),
            context: { alternativeHtml },
        })
    })
}
