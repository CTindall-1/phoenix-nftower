process AMRFINDERPLUS_UPDATE {
    tag "update"
    label 'process_low'
    container "${ workflow.containerEngine == 'singularity' && !task.ext.singularity_pull_docker_container ?
        'https://depot.galaxyproject.org/singularity/ncbi-amrfinderplus%3A3.10.40--h6e70893_1':
        'quay.io/biocontainers/ncbi-amrfinderplus:3.10.40--h6e70893_1' }"

    output:
    path "amrfinderdb.tar.gz", emit: db
    path "versions.yml"      , emit: versions

    when:
    task.ext.when == null || task.ext.when

    script:
    def args = task.ext.args ?: ''
    """
    mkdir amrfinderdb
    amrfinder_update -d amrfinderdb
    tar czvf amrfinderdb.tar.gz -C \$(readlink amrfinderdb/latest) ./

    cat <<-END_VERSIONS > versions.yml
    "${task.process}":
        amrfinderplus: \$(amrfinder --version)
        amrfinderplus_db_version: \$(head amrfinderdb/latest/version.txt)
    END_VERSIONS
    """
}
